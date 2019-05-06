/*
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/

function firstMissingPosInt(arr) { 
  let num;
  console.log(arr);
  for(let i = 0; i < arr.length; i++) { 
    console.log(arr[i])
    if(1 <= arr[i] && arr[i] <= arr.length) {  

      console.log('hhhhhh')
      console.log(arr[i]);
      console.log(arr[arr[i]-1]);
      console.log('hhhhhh')

      let temp = arr[i];
      arr[i] = arr[temp-1];
      arr[temp-1] = temp;
    }
    console.log(arr);
  }  
  console.log(arr);
  for(let i = 0; i < arr.length; i++) { 
    if(arr[i]-1 != i) { 
      num = i + 1;
      break;
    }
  }

  return num;
}

let arr = [3,4,-1,1];

console.log(firstMissingPosInt(arr));