/*
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except 
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
*/

// core idea: running product from both left and right sides
function productPerIndex(arr) {
  
  // lol, JS array default value intialization
  let leftArr = (new Array(arr.length)).fill(1);
  let rightArr = (new Array(arr.length)).fill(1);

  for(let i = 1; i < arr.length; i++) { 
    leftArr[i] = leftArr[i-1] * arr[i-1];
  }
  for(let i = arr.length-2; i >= 0; i--) { 
    rightArr[i] = rightArr[i+1] * arr[i+1];
  }

  let new_arr = new Array(arr.length);
  for(let i = 0; i < new_arr.length; i++) {
    new_arr[i] = leftArr[i] * rightArr[i];
  }  
  return new_arr;
}

let arr = [1,2,3,4,5];

console.log(`original array: ${arr}`);
console.log(`new array: ${productPerIndex(arr)}`);

