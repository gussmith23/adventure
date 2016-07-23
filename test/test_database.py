import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from database import Database

class TestDatabase(unittest.TestCase):
	def test_query(self):
		# arrange
		db = Database()
		
		# act
		created = db.query("CREATE TABLE test_table (text_field TEXT, int_field INTEGER, real_field REAL)")[0]
		unused, lastrowid, rowcount, unused = \
				db.query("INSERT INTO test_table (rowid, text_field, int_field, real_field) VALUES (?, ?, ?, ?)", 
													(1, "hi", 2, 0.5))
		entries = db.query("SELECT rowid, text_field, int_field, real_field FROM test_table WHERE rowid=1")[3]
		
		# assert
		self.assertTrue(created)
		self.assertEqual(lastrowid, 1)
		self.assertEqual(len(entries), 1)
		self.assertEqual(entries[0], (1, "hi", 2, 0.5))
		
	def test_bad_syntax_returns_false(self):
		# arrange
		db = Database()
		
		# act
		success, unused, unused, unused = db.query("Rosencrants")
		
		# assert
		self.assertFalse(success)
		