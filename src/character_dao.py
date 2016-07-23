class CharacterDao:
	def __init__(self, character_table):
		self.__character_table = character_table
		self.__characters = {}
		
	def update_character(self, character):
		success = self.__character_table.update_character(id = character._id, owner = character.owner,
								name = character.name, description = character.description)
		if not success:
			return False
		self.__characters[character.id] = character
		return True

	def get_character(self, id):
		"""Return the Character with the given id.
		
		Returns None if the character was not found, either because the character
		is not in the database or because of a database error.
		"""
		if id in self.__characters:
			return self.__characters[id]
		fields = self.__character_table.get_character(id)
		if not fields:
			return None
		character = Character(name = fields['name'], description = fields['description'],
											id = fields['id'], owner = fields['owner'])
		self.__characters[id] = character
		return character
											
	def add_character(self, character):
		"""
		
		Returns False if character's id is already set, implying the character
		came from the database or was added to the database already.
		"""
		if character.id is not None:
			return False
		fields = {
			character_table.NAME_COLUMN_KEY : character.name,
			character_table.DESC_COLUMN_KEY	: character.description,
      character_table.OWNER_COLUMN_KEY : character.owner,
		}
		rowid = character_table.add_character(fields)
		if rowid is False:
			return False
		character.id = rowid
		return True