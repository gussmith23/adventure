from character_dao import CharacterDAO

class DAOManager:
	def __init__(self, database):
		daos = {}
		daos['character'] = CharacterDAO(database.tables['character'])