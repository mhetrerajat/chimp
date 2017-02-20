from __future__ import division

from .converter import Converter
from .exceptions.temperature import TemperatureUnitNotFound
from .units import TEMPERATURE_UNITS

class Temperature(Converter):
	"""
		Attributes:
			default_unit (str, optional) : Set default temperature unit
			target_unit (str, optional) : Set target temperature unit
	"""
	def __init__(self, default_unit=None, target_unit=None):
		"""
			Initialize temperature instance

			Args:
				_conversion_of (str, private): As it is about temperature conversion, its value is temperature
				_input_lower_limit (float, private): Minimum possible value of input that is acceptable
				_input_upper_limit (float, private): Maximum possible value of input that is acceptable
		"""
		self._conversion_of = "temperature"
		self._input_lower_limit = None
		self._input_upper_limit = None
		super(Temperature, self).__init__(default_unit=default_unit, target_unit=target_unit, _conversion_of=self._conversion_of, _input_upper_limit=self._input_upper_limit, _input_lower_limit=self._input_lower_limit)

	
	def _validate_unit(self, unit):
		"""
			Check whether given unit is valid temperature unit

			Args:
				unit (str) : Unit of temperature

			Returns:
				unit if successful else raise TemperatureUnitNotFound Exception
		"""
		_unit = TEMPERATURE_UNITS.get(unit)
		if _unit:
			return unit
		else:
			raise TemperatureUnitNotFound(unit)


	def convert(self, value, to=None, from_=None):
		"""
			Convert value from one unit to another

			Args:
				value (float) : Value to be converted
				to (str) : Unit to which value will get converted
				from_ (str) : Unit from which value will get convert.

			Returns:
				converted value if successful else appropriate exception will be thrown 
		"""
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
		elif from_unit == 'c' and to_unit == 'd':
			return self.celsius_to_delisle(value)
		elif from_unit == 'c' and to_unit == 'n':
			return self.celsius_to_newton(value)
		elif from_unit == 'c' and to_unit == 'ro':
			return self.celsius_to_romer(value)
		elif from_unit == 'f' and to_unit == 'c':
			return self.fahrenheit_to_celsius(value)
		elif from_unit == 'f' and to_unit == 'k':
			return self.fahrenheit_to_kelvin(value)
		elif from_unit == 'f' and to_unit == 'ra':
			return self.fahrenheit_to_rankine(value)
		elif from_unit == 'f' and to_unit == 're':
			return self.fahrenheit_to_reaumur(value)
		elif from_unit == 'f' and to_unit == 'd':
			return self.fahrenheit_to_delisle(value)
		elif from_unit == 'f' and to_unit == 'n':
			return self.fahrenheit_to_newton(value)
		elif from_unit == 'f' and to_unit == 'ro':
			return self.fahrenheit_to_romer(value)
		elif from_unit == 'k' and to_unit == 'f':
			return self.kelvin_to_fahrenheit(value)
		elif from_unit == 'k' and to_unit == 'c':
			return self.kelvin_to_celsius(value)
		elif from_unit == 'k' and to_unit == 'ra':
			return self.kelvin_to_rankine(value)
		elif from_unit == 'k' and to_unit == 're':
			return self.kelvin_to_reaumur(value)
		elif from_unit == 'k' and to_unit == 'd':
			return self.kelvin_to_delisle(value)
		elif from_unit == 'k' and to_unit == 'n':
			return self.kelvin_to_newton(value)
		elif from_unit == 'k' and to_unit == 'ro':
			return self.kelvin_to_romer(value)
		elif from_unit == 'ra' and to_unit == 'c':
			return self.rankine_to_celsius(value)
		elif from_unit == 'ra' and to_unit == 'f':
			return self.rankine_to_fahrenheit(value)
		elif from_unit == 'ra' and to_unit == 'k':
			return self.rankine_to_kelvin(value)
		elif from_unit == 'ra' and to_unit == 're':
			return self.rankine_to_reaumur(value)
		elif from_unit == 'ra' and to_unit == 'd':
			return self.rankine_to_delisle(value)
		elif from_unit == 'ra' and to_unit == 'n':
			return self.rankine_to_newton(value)
		elif from_unit == 'ra' and to_unit == 'ro':
			return self.rankine_to_newton(value)
		elif from_unit == 're' and to_unit == 'c':
			return self.reaumur_to_celsius(value)
		elif from_unit == 're' and to_unit == 'f':
			return self.reaumur_to_fahrenheit(value)
		elif from_unit == 're' and to_unit == 'k':
			return self.reaumur_to_kelvin(value)
		elif from_unit == 're' and to_unit == 'ra':
			return self.reaumur_to_rankine(value)
		elif from_unit == 're' and to_unit == 'd':
			return self.reaumur_to_delisle(value)
		elif from_unit == 're' and to_unit == 'n':
			return self.reaumur_to_newton(value)
		elif from_unit == 're' and to_unit == 'ro':
			return self.reaumur_to_romer(value)
		elif from_unit == 'd' and to_unit == 'c':
			return self.delisle_to_celsius(value)
		elif from_unit == 'd' and to_unit == 'f':
			return self.delisle_to_fahrenheit(value)
		elif from_unit == 'd' and to_unit == 'k':
			return self.delisle_to_kelvin(value)
		elif from_unit == 'd' and to_unit == 'ra':
			return self.delisle_to_rankine(value)
		elif from_unit == 'd' and to_unit == 're':
			return self.delisle_to_reaumur(value)
		elif from_unit == 'd' and to_unit == 'n':
			return self.delisle_to_newton(value)
		elif from_unit == 'd' and to_unit == 'ro':
			return self.delisle_to_romer(value)
		elif from_unit == 'n' and to_unit == 'c':
			return self.newton_to_celsius(value)
		elif from_unit == 'n' and to_unit == 'f':
			return self.newton_to_fahrenheit(value)
		elif from_unit == 'n' and to_unit == 'k':
			return self.newton_to_kelvin(value)
		elif from_unit == 'n' and to_unit == 'ra':
			return self.newton_to_rankine(value)
		elif from_unit == 'n' and to_unit == 're':
			return self.newton_to_reaumur(value)
		elif from_unit == 'n' and to_unit == 'd':
			return self.newton_to_delisle(value)
		elif from_unit == 'n' and to_unit == 'ro':
			return self.newton_to_romer(value)
		elif from_unit == 'ro' and to_unit == 'c':
			return self.romer_to_celsius(value)
		elif from_unit == 'ro' and to_unit == 'f':
			return self.romer_to_fahrenheit(value)
		elif from_unit == 'ro' and to_unit == 'k':
			return self.romer_to_kelvin(value)
		elif from_unit == 'ro' and to_unit == 'ra':
			return self.romer_to_rankine(value)
		elif from_unit == 'ro' and to_unit == 're':
			return self.romer_to_reaumur(value)
		elif from_unit == 'ro' and to_unit == 'd':
			return self.romer_to_delisle(value)
		elif from_unit == 'ro' and to_unit == 'n':
			return self.romer_to_newton(value)
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

	def celsius_to_delisle(self, value):
		# Celsius -> Delisle
		_input_value = self._get_input(value)
		return (100 - _input_value) * 5/3

	def celsius_to_newton(self, value):
		# Celsius -> Newton
		_input_value = self._get_input(value)
		return (_input_value * 21/40) + 7.5

	def celsius_to_romer(self, value):
		# Celsius -> Romer
		_input_value = self._get_input(value)
		return _input_value * 33/100

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

	def fahrenheit_to_delisle(self, value):
		# Fahrenheit -> Delisle
		_input_value = self._get_input(value)
		return (212 - _input_value) * 5/6

	def fahrenheit_to_newton(self, value):
		# Fahrenheit -> Newton
		_input_value = self._get_input(value)
		return (_input_value - 32) * 11/60

	def fahrenheit_to_romer(self, value):
		# Fahrenheit -> Romer
		_input_value = self._get_input(value)
		return ((_input_value - 32) * 7/24) + 7.5

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

	def kelvin_to_delisle(self, value):
		# Kelvin -> Delisle
		_input_value = self._get_input(value)
		return (373.15 - _input_value) * 3/2

	def kelvin_to_newton(self, value):
		# Kelvin -> Newton
		_input_value = self._get_input(value)
		return (_input_value - 273.15) * 33/100

	def kelvin_to_romer(self, value):
		# Kelvin -> Romer
		_input_value = self._get_input(value)
		return (_input_value - 273.15) * 21/40 + 7.5

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

	def rankine_to_delisle(self, value):
		_input_value = self._get_input(value)
		return (671.67 - _input_value) * 5/6

	def rankine_to_newton(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 491.67) * 11/60

	def rankine_to_romer(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 491.67) * 7/24 + 7.5

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

	def reaumur_to_delisle(self, value):
		_input_value = self._get_input(value)
		return (80 - _input_value) * 1.875

	def reaumur_to_newton(self, value):
		_input_value = self._get_input(value)
		return _input_value * 33/80

	def reaumur_to_romer(self, value):
		_input_value = self._get_input(value)
		return _input_value * 21/32 + 7.5


	def delisle_to_celsius(self, value):
		_input_value = self._get_input(value)
		return 100 - _input_value * 2/3

	def delisle_to_kelvin(self, value):
		_input_value = self._get_input(value)
		return 373.15 - _input_value * 2/3

	def delisle_to_fahrenheit(self, value):
		_input_value = self._get_input(value)
		return 212 - _input_value * 1.2

	def delisle_to_rankine(self, value):
		_input_value = self._get_input(value)
		return 671.67 - _input_value * 1.2

	def delisle_to_newton(self, value):
		_input_value = self._get_input(value)
		return 33 - _input_value * 0.22

	def delisle_to_reaumur(self, value):
		_input_value = self._get_input(value)
		return 80 - _input_value * 8/15

	def delisle_to_romer(self, value):
		_input_value = self._get_input(value)
		return 60 - _input_value * 0.35


	def newton_to_celsius(self, value):
		_input_value = self._get_input(value)
		return _input_value * 100/33

	def newton_to_fahrenheit(self, value):
		_input_value = self._get_input(value)
		return _input_value * 60/11 + 32

	def newton_to_kelvin(self, value):
		_input_value = self._get_input(value)
		return _input_value * 100/33 + 273.15

	def newton_to_rankine(self, value):
		_input_value = self._get_input(value)
		return _input_value * 60/11 + 491.67

	def newton_to_delisle(self, value):
		_input_value = self._get_input(value)
		return (33 - _input_value) * 50/11

	def newton_to_reaumur(self, value):
		_input_value = self._get_input(value)
		return _input_value * 80/33

	def newton_to_romer(self, value):
		_input_value = self._get_input(value)
		return _input_value * 35/22 + 7.5


	def romer_to_celsius(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 7.5) * 40/21

	def romer_to_fahrenheit(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 7.5) * 24/7 + 32

	def romer_to_kelvin(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 7.5)* 40/21 + 273.15

	def romer_to_rankine(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 7.5)*24/7 + 491.67

	def romer_to_reaumur(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 7.5) * 32/21

	def romer_to_newton(self, value):
		_input_value = self._get_input(value)
		return (_input_value - 7.5) * 22/35

	def romer_to_delisle(self, value):
		_input_value = self._get_input(value)
		return (60 - _input_value) * 20/7