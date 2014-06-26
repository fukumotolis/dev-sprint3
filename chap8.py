# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Lisa

def rotate_letter(letter, n):
	if letter.isupper():
		start = ord('A')		# returns Unicode integer that corresponds with letter
	elif letter.islower():
		start = ord('a')
	else:
		return letter
	c = ord(letter) - start		# calculations... don't understand 
	i = (c + n) % 26 + start
	return chr(i)				# turns the Unicode into a string again

def rotate_word(string, n):
	result = ''
	for letter in string:		# why does this just stop when letters end instead of erroring?
		result += rotate_letter(letter, n)
	return result
