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
  while(my_q.length > 0) {
    let val = my_q.shift();

    if(val === '#') {
      serialized += val + " ";
      continue;
    } else { 
      serialized += val.val + " ";
    }
    
    if(val.left) { 
      my_q.push(val.left);
    } else { 
      my_q.push('#');
    }

    if(val.right) { 
      my_q.push(val.right);
    } else { 
      my_q.push('#');
    }
  }
  return serialized;
}

function myDeserialize(serial) { 
  let serial_arr = serial.split(' ');
  
  for(let i = 0; i < serial_arr.length; i++) { 
    serial_arr[i] = new Node(serial_arr[i]);
  }

  for(let i = 0; i < serial_arr.length; i++) { 
    if(serial_arr[i] === '#') { continue; }
    let leftChildIdx = 2 * i + 1;
    let rightChildIdx = 2 * i + 2;
    if(leftChildIdx < serial_arr.length && serial_arr[leftChildIdx] !== '#') { 
      serial_arr[i].left = serial_arr[leftChildIdx];
    }
    if(rightChildIdx < serial_arr.length && serial_arr[rightChildIdx] !== '#') { 
      serial_arr[i].right = serial_arr[rightChildIdx];
    }

  }
  return serial_arr[0];
}

let root = new Node('root', new Node('left', new Node('left.left')), new Node('right'));

let s = mySerialize(root);
let d = myDeserialize(s);

console.log(s);
console.log(d.left.left.val);
