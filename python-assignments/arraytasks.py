def ascending(array):
	for count in range(len(array)): 
		for counter in range(len(array)-1):
			temp = array[counter]
			if array[counter] > array[counter + 1]:
				array[counter] = array[counter + 1]
				array[counter + 1] = temp
		return array
