# chimp 
An universal unit converter

![alt tag](https://img.shields.io/badge/chimp-beta-blue.svg)
![alt tag](https://img.shields.io/badge/version-1.2.0-lightgrey.svg)
![alt tag](https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5%2C%203.6-brightgreen.svg)

### Installation
You can install directly after cloning:
```
python setup.py install --user
```

Install with pip
```
pip install chimp
```

If you want to install for specific python version then use this,
```
python<version> -m pip install chimp
```

### Features
1. Supports inter conversion of temperature units like celsius(c), fahrenheit(f), kelvin(k), rankine(ra), reaumur(re), delisle(d), newton(n) and romer(ro).

### Demo
```
[rajatmhetre:~]$ python
Python 2.7.10 (default, Jul 30 2016, 19:40:32)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from chimp import Temperature
>>> temp_conversion = Temperature()
>>> temp_conversion.get_units()
Use 'c' for 'Celsius'
Use 'k' for 'Kelvin'
Use 'f' for 'Fahrenheit'
Use 'ra' for 'Rankine'
Use 're' for 'Reaumur'
Use 'd' for 'Delisle'
Use 'n' for 'Newton'
Use 'ro' for 'Romer'
>>> temp_conversion.convert(232, to='f', from_='c')
449.6
>>> temp_conversion.rankine_to_reaumur(232)
-115.408888889
```




