class Utils:
	def db_results_to_dict(columns, results):
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
		