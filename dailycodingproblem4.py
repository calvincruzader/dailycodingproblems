'''
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
class Solution: 
	def find_first_missing_int(self, arr):
		for idx, num in enumerate(arr): 
			if 0 <= num and num <= len(arr)-1: 
				arr[idx], arr[num-1] = arr[num-1], num # swap 

		i = 1
		while i <= len(arr): 
			if arr[i-1] != i: 
				break 
			i += 1 
		return i


x = [3,2,1,7,5,8,4]
s = Solution() 
print(s.find_first_missing_int(x))
print(x)

