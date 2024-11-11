
# Python program to remove vowels from a string
# Function to remove vowels
def rem_vowel(string):
	vowels = ['a','e','i','o','u']
	res = ""
	# result = [letter for letter in string if letter.lower() not in vowels]
	for letter in string:
		if letter not in vowels:
			res += letter
			# print(letter)

	# result = ''.join(result)
	print(res)

# Driver program
string = "Guvi Geeks Network Private Limited"
rem_vowel(string)

