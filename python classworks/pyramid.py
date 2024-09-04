number = int(input("enter a number:"))
for count in range(0,number):
	print(" ")
	for counter in range(0,number,-count):
		print("*")