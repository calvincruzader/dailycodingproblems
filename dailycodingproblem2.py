# class Solution: 
# 	def product_except_at_i(self, arr): 
# 		leftSide = [1 for _ in range(len(arr))]
# 		rightSide = [1 for _ in range(len(arr))] 

# 		productLeft = 1
# 		for i in range(len(arr)):



# 		productRight = 1
# 		for i in range(len(arr)-1, 0, -1):

# s = Solution()


x = [1,2,3,4]
for i in range(len(x)-1, -1, -1):
	print("{0} {1}".format(i, x[i]))