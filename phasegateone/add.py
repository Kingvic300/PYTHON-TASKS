digit = int(input("input a three digit number: "))
if digit>0 and digit<1000:
	number = digit
	digit1 = number%10
	digit2 = number//10
	digit3 = digit2%10
	digit4 = digit2//10
	add = digit1+digit3+digit4
	print(add)
else:
	print("ERROR")