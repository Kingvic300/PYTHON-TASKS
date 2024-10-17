try:
	row = int(input("Enter size of row "))
	column = int(input("Enter size of column "))
	if row < 0 and column < 0:
		print("ERROR")
	else:
		for count in range(row):
			for counter in range(column):
				print(f'{count * counter}\t', end=' ')
			print()
except Exception:
	print("ERROR")
	