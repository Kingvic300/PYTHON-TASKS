import string
import random

def generates_password():
	password = ""
	letters = string.printable 
	for count in range(16):
		password += random.choice(letters)

	return password


print(generates_password())