class GameOwnerTable:
	OWNER_ID_COLUMN_KEY	= 'owner_id'
	GAME_ID_COLUMN_KEY 		= 'game_id'
	schema = {
		'name' : 'game_owner',
		'columns' : [
			{
				'column_name' 		: 		OWNER_ID_COLUMN_KEY,
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
		
	# This does not handle creating the owner/game beforehand.
	def add_owner_to_game(self, game_id, owner_id):
		query = "INSERT INTO " + self.schema['name'] \
			+ " (" + OWNER_ID_COLUMN_KEY + "," + GAME_ID_COLUMN_KEY + ") "\
			+ "VALUES (?,?)"
		return_list = []
		self._db.add_query( (query, [owner_id,game_id], return_list) )
		while len(return_list) == 0: pass
		return return_list