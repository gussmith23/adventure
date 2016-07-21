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
		
	# False if invalid id
	# None if character not found
	def get_character(self, id = -1):
		if id <= 0: 
			return False
			
		# Query for character.
		# TODO(gus): why does sqlite3 throw an error when table name is a placeholder?
		query = "SELECT " + ','.join([a['column_name'] for a in self.schema['columns']])\
			+ " FROM " + self.schema['name']\
			+ " WHERE " + self.ID_COLUMN_KEY + "=? LIMIT 1"
		return_list = []
		self._db.add_query( (query, [id], return_list) )
		while len(return_list) == 0: pass
		raw_entry = return_list[1]
		
		if not raw_entry:
			return None
		
		return Utils.db_results_to_dict(self.schema['columns'], raw_entry)
	
	# False for invalid input or error.
	# Returns rowid of added character.
	def add_character(self, fields):
		if fields is None:
			return False
				
		query = "INSERT INTO {} ({}) VALUES ({})"\
			.format(self.schema['name'],
				", ".join(fields.keys()),
				("?,"* len(fields))[:-1])
		return_list = []
		self._db.add_query( (query, tuple(fields.values()), return_list) )
		while len(return_list) == 0: pass
		
		if len(return_list) >= 2 and not return_list[1]:
			return False
			
		return return_list[0]
			
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
		
		update = "UPDATE {} ".format(self.schema['name'])
		set = "SET " + ", ".join(new_vals)
		where = "WHERE " + self.ID_COLUMN_KEY + " = ? "
		args.append(id)
		
		return_list = []
		
		self._db.add_query((update + set + where, tuple(args), return_list))
		
		while not len(return_list):
			pass
			
		return return_list[0]
		
		
		