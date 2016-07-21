class ChatTable:
	schema = {
		'name' : 'chat',
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
		self.db = db