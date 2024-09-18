count = 0
for counter in range(10):
	score = int(input("Enter your score:"))
	if score<0 or score>100:
		count+=score
print(count)