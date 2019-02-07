class Solution: 
	def uniqueWaysToClimb(self, steps, X = None):
		dp = [0 for _ in range(steps+1)]
		dp[0] = 1
		for step in range(1, steps+1, 1):
			dp[step] += sum(dp[step-x] if step-x > 0 else 0 for x in X)
			dp[step] += 1 if step in X else 0
		print(dp)
		return dp[steps]


s = Solution()
# print(s.uniqueWaysToClimb({1,2}, 4))

print(s.uniqueWaysToClimb(4, {1,2}))

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:
# Should build up to 4 from 1, 2, 3, 4, etc., always use the first few values as something to use 
#		the subproblems are the SOLUTIONS to the number of previous steps since they are similar principle...... oooooookayyyyy i totally forgot to think about it this way.
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# can't let what I know previously stop me from coming up with new solutions.
