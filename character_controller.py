"""
CharacterController
Manages characters via several provided functions:
* Create character
* Change character setting
* Get character
"""
class CharacterController:
	def __init__(self, db):
		self._db = db
		self._characters = {}
		
	def create_character(self, name, description, owner_id):
		pass
		