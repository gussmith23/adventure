class ChatGameTable:
	CHAT_ID_COLUMN_KEY	= 'chat_id'
	GAME_ID_COLUMN_KEY 		= 'id'
	schema = {
		'name' : 'chat_game',
		'columns' : [
			{
				'column_name' 		: 		CHAT_ID_COLUMN_KEY,
				'datatype' 				: 		'INTEGER',
				'null'						: 		'NOT NULL'
			},		
			{		
				'column_name' 		:	 		GAME_ID_COLUMN_KEY,
				'datatype' 				: 		'INTEGER',
				'null'						:			'NOT NULL'
			}	
		],
		'constraints' : [
			{		
				'name'						:			'pk_id',
				'type'						:			'PRIMARY KEY',
				'columns'					:			[CHAT_ID_COLUMN_KEY, GAME_ID_COLUMN_KEY]
			},
			{		
				'name'						:			'fk_game_id',
				'type'						:			'FOREIGN KEY',
				'columns'					:			[GAME_ID_COLUMN_KEY],
				'foreign-table'		:			'game',
				'foreign-columns'	:			['id']
			},
			{		
				'name'						:			'fk_chat_id',
				'type'						:			'FOREIGN KEY',
				'columns'					:			[CHAT_ID_COLUMN_KEY],
				'foreign-table'		:			'chat',
				'foreign-columns'	:			['id']
			}
		]
	}
	
	def __init__(self, db):
		self._db = db