array = [2,1,7,5,3]
for count in range(len(array)):
	array1 = array[count] * array[count]
	print(array1,end=' ')
print()
for count in range(len(array)): 
	for counter in range(len(array)-1):
		temp = array[counter]
		if array[counter] > array[counter + 1]:
			array[counter] = array[counter + 1]
			array[counter + 1] = temp
print(array)
for count in range(len(array)): 
	for counter in range(len(array)-1):
		temp = array[counter]
		if array[counter] < array[counter + 1]:
			array[counter] = array[counter + 1]
			array[counter + 1] = temp
print(array)


	