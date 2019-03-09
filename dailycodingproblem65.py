'''
Print a twoD array in a clockwise spiral 
'''

class Solution: 
  def print_matrix_clockwise_spiral(self, twoD_arr): 
    if len(twoD_arr) < 1 or len(twoD_arr[0]) < 1: 
      return 

    traversed = [[False for _col in range(len(twoD_arr[0]))] for _row in range(len(twoD_arr))]

    moves = [[0,1], [1,0], [0,-1], [-1,0]]

    moves_available = True
    move_idx = 0
    current_row, current_col = 0, 0
    traversed[current_row][current_col] = True

    print(twoD_arr[current_row][current_col])
    while moves_available: 
      row, col =  moves[move_idx][0], moves[move_idx][1]
      current_row += row
      current_col += col
      if current_row < len(twoD_arr) and current_col < len(twoD_arr[0]) and not traversed[current_row][current_col]: 
        print(twoD_arr[current_row][current_col])
        traversed[current_row][current_col] = True  
      else: 
        current_row -= row
        current_col -= col
        move_idx = (move_idx + 1) % 4 
        # peek next idx
        peek_row, peek_col = current_row + moves[move_idx][0], current_col + moves[move_idx][1]
        if peek_row >= len(twoD_arr) or peek_col >= len(twoD_arr[0]) or traversed[peek_row][peek_col]:  
          moves_available = False 


x  = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

s = Solution() 
s.print_matrix_clockwise_spiral(x)