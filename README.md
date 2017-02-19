# chimp
An universal unit converter

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
1. Supports inter conversion of temperature units like celsius(c), fahrenheit(f) and kelvin(k) 

### Demo
```
[rajatmhetre:~]$ python
Python 2.7.10 (default, Jul 30 2016, 19:40:32)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from chimp import Temperature
>>> temp_conversion = Temperature()
>>> temp_conversion.convert(232, to='f', from_='c')
449.6
>>>
```




