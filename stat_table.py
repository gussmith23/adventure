class StatTable:
	schema = {
		'name' : 'stat',
		'columns' : [
			{
				'column_name'			:			'value',
				'datatype'				:			'INTEGER'
			},		
			{		
				'column_name' 		: 		'character_id',
				'datatype' 				: 		'INTEGER'
			},		
			{		
				'column_name'			:			'game_id',
				'datatype'				:			'INTEGER'
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
				'name'						:			'fk_character',
				'type'						:			'FOREIGN KEY',
				'columns'					:			['character_id'],
				'foreign-table'		:			'character',
				'foreign-columns'	:			['id']
			},		
			{		
				'name'						:			'fk_game',
				'type'						:			'FOREIGN KEY',
				'columns'					:			['game_id'],
				'foreign-table'		:			'game',
				'foreign-columns'	:			['id']
			}
		]
	}