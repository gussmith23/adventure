class CharacterTable:
	schema = {
		'name' : 'characters',
		'columns' : [
			{
				'column_name' :  'name',
				'datatype' : 'VARCHAR(255)'
			},
			{
				'column_name' : 'owner_id',
				'datatype' : 'INTEGER'
			},		
			{		
				'column_name' 		:	 		'id',
				'datatype' 				: 		'INTEGER'
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