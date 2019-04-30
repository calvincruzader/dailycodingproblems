/*
Level: Medium
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
*/

class Node { 
  constructor(val, left, right) { 
    this.val = val; 
    this.left = left;
    this.right = right;
  }
}

function mySerialize(root) { 
  let my_q = [];
  my_q.push(root);
  let serialized = '';
  while(my_q) {

    let val = my_q.shift();
  
    serialized += val;
    if(val === '#') continue; 
    
    if(my_q.left) { 
      my_q.push(my_q.left);
    } else { 
      my_q.push('#');
    }

    if(my_q.right) { 
      my_q.push(my_q.right);
    } else { 
      my_q.push('#');
    }
    break;
  }
  return serialized;
}

let root = new Node('root', new Node('left', new Node('left.left')), new Node('right'));
console.log(mySerialize(root)); 





