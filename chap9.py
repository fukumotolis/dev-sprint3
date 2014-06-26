# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Lisa

""" 
Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).

Exercise 9.2. Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
Modify your program from the previous section to print only the words that have no “e” and com- pute the percentage of the words in the list have no “e.”

Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
"""

# 9.1

def long_words():
	fin = open(words.txt)
	for line in fin:
		word = line.strip()
		if len.word >= 20:
			print word
		else:
			long_words
# 9.2

def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

# 9.3

def avoids(word, string):
	for letter in word:
		if letter in string:
			return False
	return True

# 9.4

def uses_only(word, string):
	for letter in word:
		if letter not in string:
			return False
	return True

#  Did not address: Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?” 

