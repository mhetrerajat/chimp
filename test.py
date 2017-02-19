from chimp import Temperature


if __name__ == '__main__':
	temp = Temperature(default_unit='c')
	val = temp.convert(23,'c')
	print(val)