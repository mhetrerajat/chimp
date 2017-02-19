class NotAnNumericValue(ValueError):
	def __init__(self, *args):
		self.message = "{0} is not an numeric value".format(args)



class ValueOutOfBound(ValueError):
	def __init__(self, error_message):
		self.message = error_message


class InvalidUnitType(Exception):
	def __init__(self, *args):
		self.message = "{0} is not an valid unit type".format(args)


class InvalidConversionUnit(Exception):
	def __init__(self, *args):
		self.message = "{0} is not valid unit for {1}".format(args)


class ConversionUnitMissing(Exception):
	def __init__(self, *args):
		self.message = '"{0}" unit is missing for {1}'.format(args)


class InputValueMissing(Exception):
	def __init__(self):
		self.message = "Please provide value you wish to convert."