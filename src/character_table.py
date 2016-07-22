from utils import Utils

class CharacterTable:
	NAME_COLUMN_KEY 	= 'name'
	DESC_COLUMN_KEY		= 'description'
	OWNER_COLUMN_KEY	= 'owner_id'
	ID_COLUMN_KEY 		= 'id'
	schema = {
		'name' : 'character',
		'columns' : [
			{
				'column_name' 		:  		NAME_COLUMN_KEY,
				'datatype' 				: 		'VARCHAR(255)'
			},
			{
				'column_name'			:			DESC_COLUMN_KEY,
				'datatype'				:			'TEXT',
				'null'						:			'NULL'
			},
			{
				'column_name' 		: 		OWNER_COLUMN_KEY,
				'datatype' 				: 		'INTEGER',
				'null'						: 		'NOT NULL'
			},		
			{		
				'column_name' 		:	 		ID_COLUMN_KEY,
				'datatype' 				: 		'INTEGER',
				'null'						:			'NOT NULL'
			}	
		],
		'constraints' : [
			{		
				'name'						:			'pk_id',
				'type'						:			'PRIMARY KEY',
				'columns'					:			['id']
			},
			{		
				'name'						:			'fk_owner',
				'type'						:			'FOREIGN KEY',
				'columns'					:			['owner_id'],
				'foreign-table'		:			'user',
				'foreign-columns'	:			['id']
			}
		]
	}
	column_names = [c['column_name'] for c in schema['columns']]
	
	
	def __init__(self, db):
		self._db = db
		
	def get_character(self, id = -1):
		"""Get from the database all columns for the given character id.

		Returns a dictionary where keys are the column names.
		Returns False if there is an error, or if the number of fields returned is
		not equal to the number of columns in the table.
		Returns None if character not found.
		"""
		if id <= 0: 
			return False
			
		columns = self.schema['columns']
			
		# TODO(gus): why does sqlite3 throw an error when table name is a placeholder?
		query = "SELECT " + ','.join(self.column_names) \
			+ " FROM " + self.schema['name'] \
			+ " WHERE " + self.ID_COLUMN_KEY + "=?" \
			+ " LIMIT 1"
		success, unused, unused, entries = self._db.query(query, (id,))
		
		# These checks should be done in this order.
		if not success:
			return False
		if len(entries) == 0:
			return None
		if len(entries[0]) is not len(columns):
			return False
		else:
			return Utils.db_results_to_dict(columns, entries[0])
	
	def add_character(self, fields):
		"""Adds character to database with given fields.
		
		Returns rowid of added character.
		Returns false if there was an error.
		"""
		if type(fields) is not dict:
			return False
			
		query = "INSERT INTO {} ({}) VALUES ({})"\
			.format(self.schema['name'],
							", ".join(fields.keys()),
							("?,"* len(fields))[:-1])
		success, lastrowid, unused, unused = self._db.query(query, tuple(fields.values()))
		
		if success:
			return lastrowid
		else:
			return False
			
	def update_character(self, id, name = None, desc = None, owner = None):
		"""Update character with given data.
		
		Returns true on success, false on failure.
		"""
		if id <= 0:
			return False
		
		new_vals = []
		args = []
		if name:
			new_vals.append(self.NAME_COLUMN_KEY + " = ?")
			args.append(name)
		if desc:
			new_vals.append(self.DESC_COLUMN_KEY + " = ?")
			args.append(desc)
		if owner:
			new_vals.append(self.OWNER_COLUMN_KEY + " = ?")
			args.append(owner)
		
		update = "UPDATE {} ".format(self.schema['name'])
		set = "SET {} ".format(", ".join(new_vals))
		where = "WHERE {} = ? ".format(self.ID_COLUMN_KEY)
		args.append(id)
				
		success, unused, rowcount, unused = self._db.query(update + set + where, tuple(args))
		
		return success and (rowcount > 0)
		