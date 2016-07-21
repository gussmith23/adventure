class CharacterDAO:
	def __init__(self, character_table):
		self._character_table = character_table
		
	def update_character(self, character):
		return self._character_table.update_character(id = character._id, owner = character.owner,
																										name = character.name, description = character.description)
		
	def get_character(self, id):
		fields = self._character_table.get_character(id)
		return Character(name = fields['name'], description = fields['description'],
											id = fields['id'], owner = fields['owner'])