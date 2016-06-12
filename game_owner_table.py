class GameOwnerTable:
	OWNER_ID_COLUMN_KEY	= 'owner_id'
	GAME_ID_COLUMN_KEY 		= 'game_id'
	schema = {
		'name' : 'game_owner',
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
				'columns'					:			[OWNER_ID_COLUMN_KEY, GAME_ID_COLUMN_KEY]
			},
			{		
				'name'						:			'fk_game_id',
				'type'						:			'FOREIGN KEY',
				'columns'					:			[GAME_ID_COLUMN_KEY],
				'foreign-table'		:			'game',
				'foreign-columns'	:			['id']
			},
			{		
				'name'						:			'fk_owner_id',
				'type'						:			'FOREIGN KEY',
				'columns'					:			[OWNER_ID_COLUMN_KEY],
				'foreign-table'		:			'user',
				'foreign-columns'	:			['id']
			}
		]
	}
	
	def __init__(self, db):
		self._db = db