def factorial(number):
	factor = 0
	for count in range(number):
		if count % number ==0:
			factor+=1
	return factor
print(factorial(100))