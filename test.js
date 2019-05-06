function karatsuba_multiplication(num1, num2) { 

  // base case 
  if (num1 < 10 && num2 < 10) { 
    return num1 * num2;
  }

  let n = Math.max(String(num1).length, String(num2).length);
  let m = parseInt(Math.ceil(n/2))

  let num1_h = parseInt(Math.floor(num1 / Math.pow(10, m)));
  let num1_l = parseInt(num1 % Math.pow(10,m));

  let num2_h = parseInt(Math.floor(num2 / Math.pow(10, m)));
  let num2_l = parseInt(num2 % Math.pow(10, m));

  let a = karatsuba_multiplication(num1_h, num2_h);
  let d = karatsuba_multiplication(num1_l, num2_l);
  let e = karatsuba_multiplication(num1_h + num1_l, num2_h + num2_l) - a - d ;

  return parseInt(a * Math.pow(10, m * 2) + e * Math.pow(10, m) + d);
};

console.log(karatsuba_multiplication('3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627'));
console.log(3141592653589793238462643383279502884197169399375105820974944592);