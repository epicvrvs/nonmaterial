class Component:
	def __init__(self, reference, index, value, fields):
		self.reference = reference
		self.index = index
		self.value = value
		self.fields = fields
		
	def get_key(self):
		return (self.reference, self.index)
