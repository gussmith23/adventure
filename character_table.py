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
			}
		],
		'constraints' : [
		]
	}