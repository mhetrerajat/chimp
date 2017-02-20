from chimp import Temperature


if __name__ == '__main__':
	temp = Temperature(default_unit='c')
	temp.get_units()
	val = temp.convert(23,'f')
	print(temp.newton_to_celsius(232))
	print(val)