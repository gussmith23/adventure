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
	def init(self, fields = None, stats = None, inventory = None):
		if fields:
			self.fields = fields
		if stats:
			self.stats = stats
		if inventory:
			self.inventory = inventory