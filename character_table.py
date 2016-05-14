class CharacterTable:
	schema = {
		'name' : 'character',
		'columns' : [
			{
				'column_name' 		:  		'name',
				'datatype' 				: 		'VARCHAR(255)'
			},
			{
				'column_name'			:			'description',
				'datatype'				:			'TEXT',
				'null'						:			'NULL'
			},
			{
				'column_name' 		: 		'owner_id',
				'datatype' 				: 		'INTEGER',
				'null'						: 		'NOT NULL'
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