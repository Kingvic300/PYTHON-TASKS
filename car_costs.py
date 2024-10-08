number = int(input("Enter costs of a car"))
if number>10000000:
	print("Your duty charge percentage is 20%")
elif number>5000000 and number<10000000:
	print("Your duty charge percentage is 15%")
elif number>2500000 and number<5000000:
	print("Your duty charge percentage is 10%")
elif number<2500000:
	print("Your duty charge percentage is 5%")