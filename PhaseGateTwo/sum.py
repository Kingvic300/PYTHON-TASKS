def sum(number1,number2): 
	integer = int(number1)
	integer2 = int(number2)
	add = integer+integer2 
	plus = str(add)
	if number1 == str and number2 == str:
		raise TypeError("invalid input")
	return plus
print(sum('23','22'))