class Trie: 
	def __init__(self, isEnd): 
		self.alpha = [null] * 26
		self.isEnd = False

class Solution: 
	def get_strings_with_prefix(self, s, strings): 
		prefixed_strings = []
		for word in strings: 
			if len(word) < len(s):
				continue
			if s == word[:len(s)]:
				prefixed_strings.append(word)
		return prefixed_strings


sol = Solution()
s = 'de'
strings = ['dog', 'deer', 'deal']

print(sol.get_strings_with_prefix(s, strings)) 