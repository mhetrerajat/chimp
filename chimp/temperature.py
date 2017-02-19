from __future__ import division

from .converter import Converter
from .exceptions.temperature import TemperatureUnitNotFound
from .units import TEMPERATURE_UNITS

class Temperature(Converter):
	def __init__(self, default_unit=None, target_unit=None):
		self._conversion_of = "temperature"
		self._input_lower_limit = None
		self._input_upper_limit = None
		super(Temperature, self).__init__(default_unit=default_unit, target_unit=target_unit, _conversion_of=self._conversion_of, _input_upper_limit=self._input_upper_limit, _input_lower_limit=self._input_lower_limit)

	
	def _validate_unit(self, unit):
		_unit = TEMPERATURE_UNITS.get(unit)
		if _unit:
			return unit
		else:
			raise TemperatureUnitNotFound(unit)


	def convert(self, value, to=None, from_=None):
		from_unit = self._validate_unit(self._get_unit(from_, "from_"))
		to_unit = self._validate_unit(self._get_unit(to, "to"))

		_input_value = self._get_input(value)

		if from_unit == 'c' and to_unit == 'c':
			return _input_value
		elif from_unit == 'c' and to_unit == 'f':
			return (_input_value * 9/5) + 32
		elif from_unit == 'c' and to_unit == 'k':
			return _input_value + 273.15
		elif from_unit == 'f' and to_unit == 'c':
			return (_input_value - 32) * 5/9
		elif from_unit == 'f' and to_unit == 'f':
			return _input_value
		elif from_unit == 'f' and to_unit == 'k':
			return (_input_value - 32) * 5/9 + 273.15
		elif from_unit == 'k' and to_unit == 'f':
			return (_input_value - 273.15) * 9/5 + 32
		elif from_unit == 'k' and to_unit == 'c':
			return _input_value - 273.15
		elif from_unit == 'k' and to_unit == 'k':
			return _input_value
		else:
			raise NotImplementedError