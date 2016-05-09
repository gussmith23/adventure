class GameTable:
	schema = {
		'name' : 'game',
		'columns' : [
			{		
				'column_name' 		:	 		'id',
				'datatype' 				: 		'INTEGER'
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