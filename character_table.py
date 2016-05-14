class CharacterTable:
	NAME_COLUMN_KEY 	= 'name'
	DESC_COLUMN_KEY		= 'description'
	OWNER_COLUMN_KEY	= 'owner_id'
	ID_COLUMN_KEY 		= 'id'
	schema = {
		'name' : 'character',
		'columns' : [
			{
				'column_name' 		:  		NAME_COLUMN_KEY,
				'datatype' 				: 		'VARCHAR(255)'
			},
			{
				'column_name'			:			DESC_COLUMN_KEY,
				'datatype'				:			'TEXT',
				'null'						:			'NULL'
			},
			{
				'column_name' 		: 		OWNER_COLUMN_KEY,
				'datatype' 				: 		'INTEGER',
				'null'						: 		'NOT NULL'
			},		
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
			},
			{		
				'name'						:			'fk_owner',
				'type'						:			'FOREIGN KEY',
				'columns'					:			['owner_id'],
				'foreign-table'		:			'user',
				'foreign-columns'	:			['id']
			}
		]
	}
	
	def __init__(self, db):
		self._db = db
		
	def get_character(id = -1):
		if id is not -1:
			pass