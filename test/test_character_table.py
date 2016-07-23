import unittest
from database import Database

class TestCharacterTable(unittest.TestCase):
	def setUp(self):
		# TODO use mocks and just verify sql statements.
		self.db = Database()
		self.table = self.db.tables['character']
	
	def test_add_and_get_character(self):
		# arrange
		fields_in = {'id' : 1, 'name' : 'gus', 'description' : 'lafefawefawef', 'owner_id' : 23}
		
		# act
		returned = self.table.add_character(fields_in)
		fields_out = self.table.get_character(1)
				
		# assert
		self.assertEqual(fields_in, fields_out)
		
	def test_update_character_not_exists(self):
		# act
		out = self.table.update_character(100, desc = "blah")
		
		# assert
		self.assertFalse(out)
	
	def test_update_bad_id(self):
		# act
		zeroOut = self.table.update_character(0, desc = "blah")
		negativeOut = self.table.update_character(-1, desc = "blah")
	
		# assert
		self.assertFalse(zeroOut)
		self.assertFalse(negativeOut)
			
	def test_update_no_data(self):
		# act
		out = self.table.update_character(1)
		
		# assert
		self.assertFalse(out)
		
	def test_update_character(self):
		# arrange
		fields_in = {'id' : 1, 'name' : 'gus', 'description' : 'lafefawefawef', 'owner_id' : 23}
		self.table.add_character(fields_in)
		
		# act
		self.table.update_character(1, desc = "test")
		
		# assert
		out = self.table.get_character(1)
		self.assertEquals(out['description'], "test")
		
	def test_get_nonexistent_character_should_return_none(self):
		# act
		out = self.table.get_character(1)
		
		#assert
		self.assertEquals(out, None)
		
	def test_get_invalid_id_should_return_none(self):
		# act
		outZero = self.table.get_character(0)
		outNegative = self.table.get_character(-1)
		
		#assert
		self.assertEquals(outZero, False)
		self.assertEquals(outNegative, False)
		