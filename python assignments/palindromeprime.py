
def prime(number):
	if number <= 1 :
		return False
	for count in range(2,number):
		if number % count == 0:
			return False
		else:
			return True
	
def palindrome(number):
	reverse = 0
	while number != 0 :
		reverse = (reverse * 10) + (number % 10)
		number = number // 10
	
		if reverse == number :
			return True
		else:
			return False

def palindrome_prime(number):
	if number < 0 :
		raise ValueError("ERROR")

	if prime(number) and palindrome(number):
		return True
	else:
		return False
	