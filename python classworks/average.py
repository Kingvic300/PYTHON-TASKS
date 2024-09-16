"""Tell the user to input three different numbers
	store it as number 1,number 2,number 3 
	find the sum of the three numbers
	divide the sum by the amount of number inputted
	display the result"""
number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
number3 = int(input("enter third number: "))
sum = number1 + number2 + number3
average = sum/3
print(average)