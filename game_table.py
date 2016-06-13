class GameTable:
	schema = {
		'name' : 'game',
		'columns' : [
			{		
				'column_name' 		:	 		'id',
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
		
	def add_game(self, fields):
		pass