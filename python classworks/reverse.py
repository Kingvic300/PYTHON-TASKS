'''name = ("mummy wa")
name = ("aw ymmum")
print(name)'''
def reversed_string(word):
	reversed_word = ''
	for number in range(len(word)-1, -1, -1):
		reversed_word += word[number]
	return reversed_word
print(reversed_string("level"))