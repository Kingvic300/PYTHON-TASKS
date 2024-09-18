count = 0
for counter in range(10):
	score = int(input("Enter your score:"))
	if score%2==0:
		score+=score
		print(score)