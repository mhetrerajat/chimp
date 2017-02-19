class TemperatureUnitNotFound(Exception):
	def __init__(self, arg):
		self.message = '{0} is not a valid temperture unit'.format(arg)