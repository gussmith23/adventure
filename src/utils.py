class Utils:
	def db_results_to_dict(columns, results):
		""" Return a dictionary with the column names as keys, and values from the
		results list.
		
		There are two preconditions which must be true about the arguments for the
		output to be correct:
		1. There must be exactly one result for each column. If there are less 
				results than columns, an exception will be thrown. If there are more,
				some of the data in results will not be in the returned dictionary.
		2. The results and the list of columns must be in the same order. 
		"""
		return_dict = {}
		for counter, column in enumerate(columns):
			val = results[counter]
			type = column['datatype']
			if type is "TEXT":
				val = str(val)
			elif type is "INTEGER":
				val = int(val)
			elif type is "REAL":
				val = float(val)
			return_dict[column['column_name']] = val
		return return_dict
		