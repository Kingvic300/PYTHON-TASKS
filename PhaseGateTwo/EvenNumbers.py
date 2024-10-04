for count in range(2000,3000):
	if count%2==0:
		number = count
		digit1 = number%10
		digit2 = number//10
		digit3 = digit2%10
		digit4 = digit2//10
		if digit1%2==0 and digit2%2==0 and digit3%2==0 and digit4%2==0:
			print(count,end=',')



