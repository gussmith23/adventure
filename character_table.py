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
		
	def get_character(self, id = -1):
		if id is not -1:
			
			# Query for character.
			# TODO(gus): why does sqlite3 throw an error when table name is a placeholder?
			query = "SELECT " + ','.join([a['column_name'] for a in self.schema['columns']])\
				+ " FROM " + self.schema['name']\
				+ " WHERE " + self.ID_COLUMN_KEY + "=? LIMIT 1"
			return_list = []
			self._db.add_query( (query, [id], return_list) )
			while len(return_list) == 0: pass
			
			# Construct return dict.
			raw_entry = return_list[0]
			return_dict = {}
			for counter, column in enumerate(self.schema['columns']):
				return_dict[column['column_name']] = raw_entry[counter]
			
			return return_dict
	
	def add_character(self, fields = None, stats = None, inventory = None):
		if fields is not None:
			query = "INSERT INTO {} ({}) VALUES ({})"\
				.format(self.schema['name'],
					", ".join(fields.keys()),
					("?,"* len(fields))[:-1])
			return_list = []
			self._db.add_query( (query, tuple(fields.values()), return_list) )
			while len(return_list) == 0: pass
			return return_list