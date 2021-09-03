'''

Given a sequence of characters, find all anagrams

Dictionary used : https://github.com/dwyl/english-words for a text file containing over 466k english words.

'''

class anagramSolver:
	def __init__(self):
		self.words = set(line.strip() for line in open("words.txt"))

	def isSubArray(self, word1, word2, n, m):
		i = 0
		j = 0
		while (i < n and j < m):

			if (word1[i] == word2[j]):

				i += 1
				j += 1

				if (j == m):
					return True
					
			else:
				i = i - j + 1
				j = 0

		return False

	def findAnagrams(self, chars):
		res = []
		chars = chars.lower()
		for word in self.words:
			if (self.isSubArray(sorted(chars), sorted(word), len(chars), len(word))):
				res.append(word)

		return res


