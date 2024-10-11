guess1 = input("Enter a number ")
guess2 = input("Enter a number ")
guess3 = input("Enter a number ")
number = [guess1, guess2, guess3]
guess = []
number1 = input("Enter numbers and put comma after any number ")
guess = number1.split(',')
if number[0] == guess[0] and number[1] == guess[1] and number[2] == guess[2]:
	print("Your price is $5000")
elif number[0] == guess[0] or number[0] == guess[1] or number[0] == guess[2] or number[1] == guess[0] or number[1] == guess[1] or number[1] == guess[2] or number[2] == guess[0] or number[2] == guess[1] or number[2] == guess[2]:
	print("Your price is $4000")
elif number[0] == guess[0] or number[1] == guess[1] or number[2] == guess[2]:
	print("you have been duped")