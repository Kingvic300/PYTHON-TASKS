def maximum(number1,number2,number3):
	smallest = number1
	if number2<number1:
		smallest = number2
	if number3<number1:
		smallest = number3
	return smallest			
print(maximum(7,2,1))
		
	 