'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

is it always a binary tree?
is it alwyas a BST?

'''
class TreeNode: 

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None 

class Solution: 


  def univalCounter(self, root): 
    if not root.left and not root.right: 
      return 1

    counter = 0 

    if (root.left.val == root.right.val and root.left.val == root.val) or \
    (not root.left and root.right.val == root.val) or \
    (not root.right and root.left.val == root.val):
      counter += 1 

    return  counter + self.univalCounter(root.left) + self.univalCounter(root.right)




myroot = TreeNode(0)
myroot.left = TreeNode(1)
myroot.right = TreeNode(0)
myroot.right.right = TreeNode(0)
myroot.right.left = TreeNode(1)
myroot.right.left.left = TreeNode(1)
myroot.right.left.right = TreeNode(1)

s = Solution() 

print(s.univalCounter(myroot))