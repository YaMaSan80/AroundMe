class Location(object):
	def __init__(self, latitude,longitude):
		self.latitude = latitude
		self.longitude = longitude
	def position(self):
		return locate(latitude,longitude)

