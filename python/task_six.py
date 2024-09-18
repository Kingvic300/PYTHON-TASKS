count = 0
for counter in range(10):
	score = int(input("Enter your score:"))
	if score%2==0:
		count+=score
average = count/10
print("your average score is: ", average)
print(count)