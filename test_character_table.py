import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from database import Database
from character_table import CharacterTable

class TestCharacterTable(unittest.TestCase):
	def setUp(self):
		# TODO use mocks and just verify sql statements.
		self.db = Database()
		self.table = CharacterTable(self.db)
	
	def test_add_and_get_character(self):
		# arrange
		fields_in = {'id' : 1, 'name' : 'gus', 'description' : 'lafefawefawef', 'owner_id' : 23}
		
		# act
		self.table.add_character(fields_in)
		fields_out = self.table.get_character(1)
		
		# assert
		self.assertEqual(fields_in, fields_out)