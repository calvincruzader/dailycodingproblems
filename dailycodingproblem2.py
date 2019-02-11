class Solution: 
  def product_except_at_i(self, arr): 
    leftSide = [1 for _ in range(len(arr))]
    rightSide = [1 for _ in range(len(arr))] 

    productLeft = 1
    for i in range(len(arr)):
      leftSide[i] = productLeft
      productLeft  *= arr[i]

    productRight = 1
    for i in range(len(x)-1, -1, -1):
      rightSide[i] = productRight 
      productRight *= arr[i]

    output = [] 
    for i in range(len(arr)): 
      output.append(leftSide[i] * rightSide[i])

    return output

s = Solution()

x = [1,2,3,4, 5]
# for i in range(len(x)-1, -1, -1):
# 	print("{0} {1}".format(i, x[i]))
#   
print(s.product_except_at_i(x))
