def number_in_between(number):
	for number in range(1,999):
		if number%2==0:
			digit1 = number%10
			digit2 = number%10
			print(digit1+digit2)
print(number_in_between("121"))		