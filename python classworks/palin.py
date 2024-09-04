digit = int(input("input a three digit number: "))
number = digit
digit1 = number%10
digit2 = number//10
digit3 = digit2%10
digit4 = digit2//10
if digit1==digit4:
	print("is palindrome")
if digit1!=digit4:
	print("is not palindrome")
