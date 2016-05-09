class UserTable:
	schema = {
		'name' : 'user',
		'columns' : [
			{
				'column_name' 		: 		'telegram_id',
				'datatype' 				: 		'INTEGER',
				'null'						:			'NOT NULL'	
			},		
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
			},
			{		
				'name'						:			'uq_telegram_id',
				'type'						:			'UNIQUE',
				'columns'					:			['telegram_id']
			}
		]
	}
	
	def __init__(self, db):
		self.db = db
	
	def add_user(self, telegram_id):
		query_str = "INSERT INTO user (telegram_id) VALUES (?)"
		query_args = [telegram_id]
		return_list = []
		self.db.add_query( (query_str, query_args, return_list) )
		while len(return_list) == 0: pass
		return return_list[0] is not False