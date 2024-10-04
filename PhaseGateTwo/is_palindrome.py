
def reverse(number):
	reverse = 0
	while number != 0 :
		reverse = (reverse * 10) + (number % 10)
		number = number // 10
	return reverse	
print(reverse(123))

def palindrome(number):
	rev = reverse(number)
	if rev == number :
		return True
	else:
		return False
print(palindrome(123))