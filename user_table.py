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
				'name':									'pk_id',
				'type':									'PRIMARY KEY',
				'columns':							['id']
			}
		]
	}