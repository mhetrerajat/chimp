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

		if from_unit == to_unit:
			# if both are same
			return self._get_input(value)
		elif from_unit == 'c' and to_unit == 'f':
			return self.celsius_to_fahrenheit(value) 
		elif from_unit == 'c' and to_unit == 'k':
			return self.celsius_to_kelvin(value)
		elif from_unit == 'c' and to_unit == 'ra':
			return self.celsius_to_rankine(value)
		elif from_unit == 'c' and to_unit == 're':
			return self.celsius_to_reaumur(value)
		elif from_unit == 'f' and to_unit == 'c':
			return self.fahrenheit_to_celsius(value)
		elif from_unit == 'f' and to_unit == 'k':
			return self.fahrenheit_to_kelvin(value)
		elif from_unit == 'f' and to_unit == 'ra':
			return self.fahrenheit_to_rankine(value)
		elif from_unit == 'f' and to_unit == 're':
			return self.fahrenheit_to_reaumur(value)
		elif from_unit == 'k' and to_unit == 'f':
			return self.kelvin_to_fahrenheit(value)
		elif from_unit == 'k' and to_unit == 'c':
			return self.kelvin_to_celsius(value)
		elif from_unit == 'k' and to_unit == 'ra':
			return self.kelvin_to_rankine(value)
		elif from_unit == 'k' and to_unit == 're':
			return self.kelvin_to_reaumur(value)
		elif from_unit == 'ra' and to_unit == 'c':
			return self.rankine_to_celsius(value)
		elif from_unit == 'ra' and to_unit == 'f':
			return self.rankine_to_fahrenheit(value)
		elif from_unit == 'ra' and to_unit == 'k':
			return self.rankine_to_kelvin(value)
		elif from_unit == 'ra' and to_unit == 're':
			return self.rankine_to_reaumur(value)
		elif from_unit == 're' and to_unit == 'c':
			return self.reaumur_to_celsius(value)
		elif from_unit == 're' and to_unit == 'f':
			return self.reaumur_to_fahrenheit(value)
		elif from_unit == 're' and to_unit == 'k':
			return self.reaumur_to_kelvin(value)
		elif from_unit == 're' and to_unit == 'ra':
			return self.reaumur_to_rankine(value)
		else:
			raise NotImplementedError


	def celsius_to_fahrenheit(self, value):
		# Celsius -> Fahrenheit
		_input_value = self._get_input(value)
		return (_input_value * 9/5) + 32

	def celsius_to_kelvin(self, value):
		# Celsius -> Kelvin
		_input_value = self._get_input(value)
		return _input_value + 273.15

	def celsius_to_rankine(self, value):
		# Celsius -> Rankine
		_input_value = self._get_input(value)
		return (_input_value * 9/5) + 491.67

	def celsius_to_reaumur(self, value):
		# Celsius -> Reaumur
		_input_value = self._get_input(value)
		return _input_value * 4/5

	def fahrenheit_to_celsius(self, value):
		# Fahrenheit -> Celsius
		_input_value = self._get_input(value)
		return (_input_value - 32) * 5/9

	def fahrenheit_to_kelvin(self, value):
		# Fahrenheit -> Kelvin
		_input_value = self._get_input(value)
		return (_input_value - 32) * 5/9 + 273.15

	def fahrenheit_to_rankine(self, value):
		# Fahrenheit -> Rankine
		_input_value = self._get_input(value)
		return _input_value + 459.67

	def fahrenheit_to_reaumur(self, value):
		# Fahrenheit -> Reaumur
		_input_value = self._get_input(value)
		return (_input_value - 32) * 4/9

	def kelvin_to_celsius(self, value):
		# Kelvin -> Celsius
		_input_value = self._get_input(value)
		return _input_value - 273.15

	def kelvin_to_fahrenheit(self, value):
		# Kelvin -> Fahrenheit
		_input_value = self._get_input(value)
		return (_input_value - 273.15) * 9/5 + 32

	def kelvin_to_rankine(self, value):
		# Kelvin -> Rankine
		_input_value = self._get_input(value)
		return _input_value * 9/5

	def kelvin_to_reaumur(self, value):
		# Kelvin -> Reaumur
		_input_value = self._get_input(value)
		return (_input_value - 273.15) * 4/5

	def rankine_to_celsius(self, value):
		# Rankine -> Celsius
		_input_value = self._get_input(value)
		return (_input_value - 491.67) * 5/9

	def rankine_to_fahrenheit(self, value):
		# Rankine -> Fahrenheit
		_input_value = self._get_input(value)
		return _input_value - 459.67

	def rankine_to_kelvin(self, value):
		# Rankine -> Kelvin
		_input_value = self._get_input(value)
		return _input_value * 5/9

	def rankine_to_reaumur(self, value):
		# Rankine -> Reaumur
		_input_value = self._get_input(value)
		return (_input_value - 32 - 459.67) * 4/9

	def reaumur_to_celsius(self, value):
		# Reaumur -> Celsius
		_input_value = self._get_input(value)
		return _input_value * 5/4

	def reaumur_to_fahrenheit(self, value):
		# Reaumur -> Fahrenheit
		_input_value = self._get_input(value)
		return (_input_value * 9/4) + 32

	def reaumur_to_kelvin(self, value):
		# Reaumur -> Kelvin
		_input_value = self._get_input(value)
		return (_input_value * 5/4) + 273.15

	def reaumur_to_rankine(self, value):
		# Reaumur -> Rankine
		_input_value = self._get_input(value)
		return (_input_value * 9/4) + 32 + 459.67