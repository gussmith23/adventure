import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
	def test_db_results_to_dict(self):
		# arrange
		raw = ["hi", "0", "0.5"]
		columns = [
			{
				'column_name'			:			"test_text",
				'datatype'				:			'TEXT',
			},
			{
				'column_name' 		: 		"test_int",
				'datatype' 				: 		'INTEGER',
			},		
			{		
				'column_name' 		:	 		"test_float",
				'datatype' 				: 		'REAL',
			}	
		]
		
		# act
		out = Utils.db_results_to_dict(columns, raw)
		
		# assert
		keys = out.keys()
		
		for column in columns:
			self.assertTrue(column['column_name'] in keys)
			
		self.assertTrue(type(out['test_text']) is str)
		self.assertTrue(type(out['test_int']) is int)
		self.assertTrue(type(out['test_float']) is float)
		