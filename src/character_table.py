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
	
	def __init__(self, db):
		self._db = db
		
	# False if invalid id or db error.
	# None if character not found
	def get_character(self, id = -1):
		if id <= 0: 
			return False
			
		# TODO(gus): why does sqlite3 throw an error when table name is a placeholder?
		query = "SELECT " + ','.join([a['column_name'] for a in self.schema['columns']])\
			+ " FROM " + self.schema['name']\
			+ " WHERE " + self.ID_COLUMN_KEY + "=? LIMIT 1"
		success, unused, unused, entries = self._db.query(query, (id,))
		
		if not success:
			return False
		if len(entries) == 0:
			return None
		else:
			return Utils.db_results_to_dict(self.schema['columns'], entries[0])
	
	# False for invalid input or error.
	# Returns rowid of added character.
	def add_character(self, fields):
		if fields is None:
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
		
		update = "UPDATE OR FAIL {} ".format(self.schema['name'])
		set = "SET {} ".format(", ".join(new_vals))
		where = "WHERE {} = ? ".format(self.ID_COLUMN_KEY)
		args.append(id)
				
		success, unused, rowcount, unused = self._db.query(update + set + where, tuple(args))
		
		return success and (rowcount > 0)
		
		
		