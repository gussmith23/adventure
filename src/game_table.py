class GameTable:
	ID_COLUMN_KEY = 'id'
	schema = {
		'name' : 'game',
		'columns' : [
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
			}
		]
	}
	
	def __init__(self, db):
		self._db = db
		
	# Returns return_list, which may or may not have entries.
	# Caller should wait on return list to have items, if they need results.
	def add_game(self, id):
		query = "INSERT INTO " + self.schema['name']\
			+ " (" + self.ID_COLUMN_KEY + ") "\
			+ "VALUES (?)"
		return_list = []
		self._db.add_query( (query, [id], return_list) )
		return return_list