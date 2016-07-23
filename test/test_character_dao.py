import unittest
from database import Database
from character_dao import CharacterDao
from character import Character

class TestCharacterDao(unittest.TestCase):
	def set_up(self):
		self.db = Database()
		self.dao = CharacterDao(self.db.tables['character'])
		
	def test_update_returns_false(self):
		character = Character()