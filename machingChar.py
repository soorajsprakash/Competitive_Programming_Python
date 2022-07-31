# Matching Characters --> CODERBYTE

# Have the function MatchingCharacters(str) take the str parameter being passed 
# and determine the largest number of unique characters that exists between a pair 
# of matching letters anywhere in the string. 
# For example: if str is "ahyjakh" then there are only two pairs of matching letters, 
# the two a's and the two h's. Between the pair of a's there are 3 unique characters: h, y, and j. 
# Between the h's there are 4 unique characters: y, j, a, and k. So for this example your program should return 4.

# Another example: if str is "ghececgkaem" then your program should return 5
# because the most unique characters exists within the farthest pair of e characters. 
# The input string may not contain any character pairs, and in that case 
# your program should just return 0. The input will only consist of lowercase alphabetic characters. 

sample = "ghececgkaem"
# sample = "ahyjakh"
# sample = "mmmerme"
# sample = "abcdefg"


def MatchingCharacters(text):
	count = 0
	print(sample)
	for letter in sample:
		sample_split = sample.rsplit(letter)
		if len(sample_split) == 3:
			if count < len(set(sample_split[1])):
				count = len(set(sample_split[1]))
		elif len(sample_split) > 3:
			q = sample_split[1:-1]
			r = "".join(q)
			if count < len(set(r)) + 1:
				count = len(set(r)) + 1
		elif len(sample_split) <= 2:
			if count < 1:
				count = 0
	return count


print(MatchingCharacters(sample))
