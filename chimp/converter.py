from .exceptions.converter import NotAnNumericValue, ValueOutOfBound, InvalidConversionUnit, InvalidUnitType, ConversionUnitMissing, InputValueMissing
from .units import TEMPERATURE_UNITS


class Converter(object):
	def __init__(self, default_unit, target_unit, _conversion_of, _input_upper_limit, _input_lower_limit):
		self.default_unit = default_unit
		self.target_unit = target_unit

		self._conversion_of = _conversion_of
		self._input_upper_limit = _input_upper_limit
		self._input_lower_limit = _input_lower_limit


	def _validate_input(self, input_value):
		if isinstance(input_value, int) or isinstance(input_value, float):
			if self._input_lower_limit:
				if input_value < self._input_lower_limit:
					raise ValueOutOfBound('Input value cannot be less than {0}'.format(self._input_lower_limit))

			if self._input_upper_limit:
				if input_value > self._input_upper_limit:
					raise ValueOutOfBound('Input value cannot be greater than {1}'.format(self._input_upper_limit))
			
			return True
		else:
			raise NotAnNumericValue


	def _get_input(self, input_value):
		_valid_input = self._validate_input(input_value)
		if _valid_input:
			return float(input_value)
		else:
			raise InputValueMissing


	def _get_unit(self, unit_val, unit_type):
		if unit_type == 'from_':
			if unit_val:
				return unit_val
			elif self.default_unit:
				return self.default_unit
			else:
				raise ConversionUnitMissing(unit_type, self._conversion_of)
		elif unit_type == 'to':
			if unit_val:
				return unit_val
			elif self.target_unit:
				return self.target_unit
			else:
				raise ConversionUnitMissing(unit_type, self._conversion_of)
		else:
			raise InvalidUnitType(unit_type)


	def get_units(self, help_=True):
		if help_:
			if self._conversion_of == 'temperature':
				print('\n'.join(["Use '{0}' for '{1}'".format(k,v) for k,v in TEMPERATURE_UNITS.items()]))
			else:
				raise NotImplementedError("Invalid conversion method")
		else:
			if self._conversion_of == 'temperature':
				print(TEMPERATURE_UNITS.keys())
			else:
				raise NotImplementedError("Invalid conversion method")

