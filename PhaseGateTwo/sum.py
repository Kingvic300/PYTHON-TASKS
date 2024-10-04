def sum(number1,number2): 
	if number1 =="" and number2 == "":
		raise TypeError("invalid input")
	integer = int(number1)
	integer2 = int(number2)
	add = integer+integer2 
	plus = str(add)
	return plus
print(sum('23','22'))