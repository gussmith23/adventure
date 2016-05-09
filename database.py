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

class Database:

	def __init__(self, db_path):
	
		# create table objects
		self.tables = {
			'character' 		: 	CharacterTable(),
			'stat'					:		StatTable(),
			'stat_type'			:		StatTypeTable(),
			'game'					:		GameTable(),
			'user'					:		UserTable()			
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
				if constraint['type'] == "PRIMARY KEY":
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
				
			# executing without arguments
			else:
				try:	
					cur.execute(query[0])
				except sqlite3.IntegrityError:
					error = True				
					
			# handle error case and exit if error 
			if error:
				query[2].extend([False])
				self.q.task_done()
				continue
					
			# if there's no return, we signal with "None"
			all = cur.fetchall()
			if (len(all) == 0): 
				query[2].extend([None])
			else:	
				query[2].extend(all)
				
			# finally, commit.
			self.conn.commit()
			
			self.q.task_done()
				