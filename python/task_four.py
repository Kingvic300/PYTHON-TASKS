count = 0
total = 0
for counter in range(10):
	score = int(input("Enter your score:"))
	if counter%2==0:
		total+=score
print("your total score is: ",total)
