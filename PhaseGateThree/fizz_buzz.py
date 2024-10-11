for count in range(1,51):
	if count % 3 == 0 and count % 5 == 0:
		print("fizz buzz")
	elif count % 3 == 0:
		print("fizz")
	elif count % 5 == 0:
		print("buzz")
	else:
		print(count)
	