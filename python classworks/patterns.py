number = int(input("enter number:"))
number += 1
space = " "
for count in range(1,number):
	for counter in range(count,1,-1):
		print(space*count, counter)
		counter -=1
for count in range(1,count,+1):
	print(space*count,counter)
