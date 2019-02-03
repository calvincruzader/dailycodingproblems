'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

class Solution:

  def countNumDecodedWays(self, mapping, msg): 
    # is the mapping always going to be between numbers and letters? 
    # is the mapping a bijection?
    if len(msg) < 1: 
      return 0 
    elif len(msg) == 1: 
      return 1
    decode = {} 

    for key in mapping: 
      decode[mapping[key]] = key




'''
Pretty sure this is DP.
Going from left to right, for the message thus far, we will count the number of ways the current code can be decoded at n and the just add on the number of ways it was
decoded at n-1

1 = a                                                   1
11 = k, aa                                              2       
111 = aaa, ka, ak                                       3      
1111 = aaaa, kaa, aka, aak, kka                         5      
11111 = aaaaa, kaaa, akaa, aaka, aaak, akk, kak, kka    8      


'''

s = Solution() 

my_mapping = {
  'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 
  'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}


