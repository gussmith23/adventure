import sqlite3
import os
import time
import queue
import threading

# database table classes
from character_table import CharacterTable
from stat_type_table import StatTypeTable
from stat_table import StatTable
from game_table	import GameTable
from user_table import UserTable
from chat_table import ChatTable
from chat_game_table import ChatGameTable
from game_owner_table import GameOwnerTable

class Database:

	def __init__(self, db_path=":memory:"):
	
		# create table objects
		self.tables = {
			'character' 		: 	CharacterTable(self),
			'stat'					:		StatTable(self),
			'stat_type'			:		StatTypeTable(self),
			'game'					:		GameTable(self),
			'user'					:		UserTable(self),
			'chat'					:		ChatTable(self),
			'chat_game'			: 	ChatGameTable(self),
			'game_owner'		:		GameOwnerTable(self),
		}
				
		self.q = queue.Queue()
		
		# setup&start thread that will handle db accesses
		t = threading.Thread(target = self.worker, args=(db_path,))
		t.daemon = True			# allows it to die with main thread
		t.start()
					
	# query structure will be a tuple with the following items:
	# first, a string query (required)
	# second, a tuple of fill-in arguments for the query (required, can be empty)
	# third, an empty list for getting return values. (required even if no returns given)
	# to get the return of the query, the user should block (while len(query[2]) == 0: pass) 
	# TODO i don't like this structure; second and third shouldn't be required
	#	TODO this whole thing should be done with concurrent.futures
	def add_query(self, query):
		self.q.put(query)
		
	def query(self, query, args = ()):
		"""Submit query and block until query completes.
		
		Returns a tuple in the following format:
		(error, lastrowid, entries_list)
		error - boolean indicating if the query resulted in an error.
		lastrowid - the row id of the last inserted item. None if there is an error.
		entries_list - the list of entries returned. None if there is an error.
		"""
		returned = []
		self.q.put( (query, args, returned) )
		while not len(returned):
			pass
		if returned[0] is True:
			return (True, returned[1], returned[2], returned[3:])
		else:
			return (False, None, None, None)
		
	def worker(self,db_path):
	
		# open connection. this object should ONLY be touched
		# by this worker loop.
		# TODO: remove 'self.' so that it's local to this loop.
		self.conn = sqlite3.connect(db_path)
		
		# create user table
		cur =  self.conn.cursor()
		
		"""cur.execute("CREATE TABLE IF NOT EXISTS users " +
								"(user_id INTEGER, " +
								"reputation INTEGER, " +
								"username TEXT," +
								"time_joined INTEGER," +
								"CONSTRAINT users_pk PRIMARY KEY (user_id))")"""
								
		# create tables
		for table in list(self.tables.values()):

			columns_string = \
				", ".join(["{} {} {}".format(a['column_name'], a['datatype'], a['null'] if 'null' in a.keys() else 'NULL')\
										for a in table.schema['columns']])
										
			constraints = []
			constraints_str = ""
			
			for constraint in table.schema['constraints']:
				# (add a space at the start to be safe)
				constraint_str = " CONSTRAINT " + constraint['name'] + " " + constraint['type'] + " "				
				if constraint['type'] == "PRIMARY KEY" or constraint['type'] == "UNIQUE":
					constraint_str += " ( " + ", ".join(constraint['columns']) + " ) "
				elif constraint['type'] == "FOREIGN KEY":	
					constraint_str += " ( " + ", ".join(constraint['columns']) + " ) "
					constraint_str += "REFERENCES " + constraint['foreign-table'] + " "
					constraint_str += " ( " + ", ".join(constraint['foreign-columns']) + " ) "
				constraints.append(constraint_str)
			
			if len(constraints) is not 0:
				constraints_str += " , "
				constraints_str += ", ".join(constraints)

			create_table_query = "CREATE TABLE IF NOT EXISTS " + table.schema['name']	+ " (" + columns_string + constraints_str + ")"
			cur.execute(create_table_query)					
			
		# don't forget to commit!
		self.conn.commit()
		
		while True:
			query = self.q.get()
			if query is None: continue
			
			cur = self.conn.cursor()
			
			error = False
			
			# executing with arguments
			if len(query) > 1:
				try:	
					cur.execute(query[0], query[1])
				except sqlite3.IntegrityError:
					error = True
				except sqlite3.OperationalError:
					error = True
			
			# executing without arguments
			else:
				try:	
					cur.execute(query[0])
				except sqlite3.IntegrityError:
					error = True
				except sqlite3.OperationalError:
					error = True
					
			"""Output format: [error, lastrowid, entries...]"""
			return_list = []
			
			# handle error case and exit if error 
			if error:
				return_list.extend([False])
				query[2].extend(return_list)
				self.q.task_done()
				continue
			else:
				return_list.extend([True])
					
			# give the last rowid
			return_list.extend([cur.lastrowid])
			return_list.extend([cur.rowcount])
			
			return_list.extend(cur.fetchall())
			
			query[2].extend(return_list)
				
			# finally, commit.
			self.conn.commit()
			
			self.q.task_done()
				