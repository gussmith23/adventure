"""
Character class
This class directly represents an entry in the character table.
"""

class Character:

	"""
	fields: a dictionary of 'fields', which are the columns of the character table.
	stats: a dictionary of stats, which are found via JOINing with the stat table.
	inventory: not yet decided
	"""
	def __init__(self, name = "", description = "", owner = -1, id = -1, stats = None, inventory = None):
		self.name = name
		self.description = description
		self._owner = owner
		self._id = id
		self.stats = stats
		self.inventory = inventory