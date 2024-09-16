score = 0
count = 0
number = float(input("enter number from 1 to 10000:"))
while number!=0:
	number = float(input("Enter 0 to end :"))
	if number>=0 and number<10000:
		score +=number
		count+=1
average = score /count
print("your average score is:", average)