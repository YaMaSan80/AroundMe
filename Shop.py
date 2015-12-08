class Shop(object):
	def __init__(self, shopID, name, type):
		self.shopID = shopID
		self.name = name
		self.type = type
	def shopID(self):
		return self(shopID)
	def name(self):
		return self(name)
	def type(self):
		return self(type)
