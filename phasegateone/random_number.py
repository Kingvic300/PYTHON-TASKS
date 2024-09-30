import random
number1 = random.randrange(100)
print(number1)
number2 = random.randrange(100)
print(number2)
sum = number1 + number2
number3 = input("Enter the sum of the numbers ")
print(sum)
if number3 == sum:
	print("True")
else:
	print("False")