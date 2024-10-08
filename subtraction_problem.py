import random
passed = 0
fail = 0
for count in range(10):


	number1 = random.randrange(30)
	print(number1)	

	number2 = random.randrange(30)
	print(number2)
	if number1 > number2:
		difference = number1 - number2
	else:
		difference = number2 - number1

	number = int(input("Find the subtraction of number1 and number2 "))
	
	if number == difference:
		print("Correct")
		passed+=1

	else:
		print("Incorrect")
		fail +=1
	print(difference)
print("You passed",passed,"times")
rint("You failed",fail,"times")
