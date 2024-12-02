'''
35538
30442

changed logic in part 2 because hyperneutrino showed a more elegant soln from what i had lmao

'''

def find_index(grid):
  for i in range(1, len(grid)):
    left = grid[:i][::-1]  # flip the left side to see if it equals the right
    right = grid[i:]

    mirror_len = min(len(left), len(right))
    left = left[:mirror_len]
    right = right[:mirror_len]
    if left == right:
      return i

  return 0


def find_smudge(grid):
  for i in range(1, len(grid)):
    left = grid[:i][::-1]  # flip the left side to see if it equals the right
    right = grid[i:]

    mirror_len = min(len(left), len(right))
    left = left[:mirror_len]
    right = right[:mirror_len]

    # if theres just 1 diff in our left and right grids we can return that index
    if sum(0 if left_indx == right_indx else 1 
      for left_row, right_row in zip(left, right)
      for left_indx, right_indx in zip(left_row, right_row)) == 1:
        return i

  return 0


def question_one():
  with open("day13.txt") as f:
    patterns = f.read().split('\n\n')
  res = 0
  for pattern in patterns:
    # create a grid from this
    grid = pattern.splitlines()

    row_patterns = list(map(list, grid))
    # similar to how to transpose a matrix 
    col_patterns = list(map(list, zip(*grid)))

    row_match_idx = find_index(row_patterns)
    col_match_idx = find_index(col_patterns) 

    if row_match_idx:
        res+= 100*row_match_idx 
    elif col_match_idx:
        res+= col_match_idx
      

  print(res)
  # 35538


def question_two():
  with open("day13.txt") as f:
    patterns = f.read().split('\n\n')
  res = 0
  for pattern in patterns:
    # create a grid from this
    grid = pattern.splitlines()

    row_patterns = list(map(list, grid))
    # transpose a matrix (shout out leetcode ;) )
    col_patterns = list(map(list, zip(*grid)))

    row_match_idx = find_smudge(row_patterns)
    col_match_idx = find_smudge(col_patterns) 

    if row_match_idx:
        res+= 100*row_match_idx 
    elif col_match_idx:
        res+= col_match_idx

  print(res)
  # 30442
      

question_one()
question_two()

