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
    output.append(root.val)

    while node_queue: 
      node = node_queue.popleft()
       
      left_child = node.left
      right_child = node.right

      if left_child:
        node_queue.append(left_child)
        output.append(left_child.val)
      else: 
        output.append('#')

      if right_child:
        node_queue.append(right_child)
        output.append(right_child.val)
      else: 
        output.append('#')

    return ' '.join(map(str, output))

  # dumbs down to connecting the nodes in the heapify() structure 
  def deserialize(self, s): 
    if not s or len(s) < 1: return None

    s_list = s.split(' ')

    node_list = []
    for s_val in s_list: 
      if s_val != '#':
        node_list.append(TreeNode(int(s_val)))
      else: 
        node_list.append('#')

    for i in range(len(node_list)):
      node = node_list[i]
      left_idx = 2 * i + 1
      right_idx = 2 * i + 2 
      if left_idx < len(node_list) and node_list[left_idx] != '#':
        node.left = node_list[left_idx]
      if right_idx < len(node_list) and node_list[right_idx] != '#':
        node.right = node_list[right_idx]

    return node_list[0]


# in order traversal sanity check
def inorder_traversal(root, output): 
  if not root: return 
  inorder_traversal(root.left, output) 
  output.append(root.val)
  inorder_traversal(root.right, output)
  return output

root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(8)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(11)

'''
         5
       /   \
      3     8
     / \   / \
    1   4 7   11

'''
print("in order traversal before any encryption:")
print(inorder_traversal(root1, []))
print("performing encryption...")
s = Encryption() 
print("serializing...")
serialized_value = s.serialize(root1)
print("serialized value: {}".format(serialized_value))
print("deserializing...")
deserialized_root = s.deserialize(serialized_value)
# print(deserialized_root.val)
print("in order traversal using the deserialized root")
print(inorder_traversal(deserialized_root, []))

'''
Preserving the property where, for all node n at index i:
left child index = 2 * i + 1 
right child index = 2 * i + 2 
was a PAIN IN THE ASS
'''

