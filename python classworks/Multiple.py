"""
PSEUDOCODE
	find the multiple of 10 from 1 to 20_000
	sum the multiple of 10 from 1 to 20_000
	display the result
"""
total = 0
for number in range (1,20001):
	if number%10==0:
		total = number +number
print(total)