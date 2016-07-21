class StatTypeTable:
	schema = {
		'name' : 'stat_type',
		'columns' : [
			{
				'column_name' :  		'name',
				'datatype' 		: 		'VARCHAR(255)'
			},
			{
				'column_name' : 		'game_id',
				'datatype' 		: 		'INTEGER'
			},
			{
				'column_name' :	 		'id',
				'datatype' 		:			'INTEGER',
				'null'				:			'NOT NULL'
			}
		],
		'constraints' : [
			{
				'name'				:			'pk_id',
				'type'				:			'PRIMARY KEY',
				'columns'			:			['id']
			}
		]
	}
	
	def __init__(self, db):
		self.db = db