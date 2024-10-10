import math
def square(number):
	if number < 0:
		raise ValueError("invalid input")
	if number == str:
		raise TypeError("invalid input")
	if number%5==0:
		return math.sqrt(number)
	else:
		division = number/5
	return division
print(square(10))
print(square(23))