/*
Level: Easy 
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Do this in one pass.
*/

// core idea: cache the future potential second number
function numsAddToK(arr, k) { 
  if(arr.length < 2) { 
    return false; 
  }
  let cache = new Set();

  // This doesn't work because .forEach() takes a callback function as parameter
  // let exists = false;
  // arr.forEach(num => {
  //   if(cache.has(num)) {
  //    exists = true;
  //   } else { 
  //     cache.add(k-num);
  //   }
  // });
  // return exists;
  
  for(let i = 0; i < arr.length; i++) { 
    let num = arr[i];
    if(cache.has(num)) { 
      return true;
    } else { 
      cache.add(k-num);
    }
  }
  return false;
}

k = 17;
my_arr = [10,15,3,7]

console.log(numsAddToK(my_arr, k));

let cache = new Set();


