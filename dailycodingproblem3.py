'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
'''
from collections import deque

class TreeNode: 
  def __init__(self, val, left=None, right=None):
    self.val, self.left, self.right = val, left, right


class Encryption: 
  def serialize(self, root): 
    output = []
    node_queue = deque()
    node_queue.append(root)

    while node_queue: 
      node = node_queue.popleft()
      
      output.append(node.val)

      left_child = node.left
      right_child = node.right

      if left_child:
        node_queue.append(left_child)
      else: 
        output.append('#')

      if right_child:
        node_queue.append(right_child)
      else: 
        output.append('#')

    return ' '.join(map(str, output))

  def deserialize(self, s): 
    return 0 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)

s = Encryption() 
print(s.serialize(root))

