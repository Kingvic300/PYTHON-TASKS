numbers = []
num = 0
while True:
	number = int(input("Enter number:"))
	if number==-1:
		break
	numbers += [number]
	num+=1
	number+=number
	average = number/num
print(numbers)
print(average)
