class Solution: 
	def addUpToK(self, nums, k): 
		compl = set() 

		for num in nums: 
			if num in compl: 
				return True 
			else: 
				compl.add(k-num)
		return False 


s = Solution() 
print(s.addUpToK([10, 15, 3, 7], 17))