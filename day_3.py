'''
Find all the numbers, store them in a hashmap as well as their coordinates
Search up,down, left, right, diagonal values around each number to find adjacement symbols, 
also make sure you are searching within the bounds of the list. If that number contains 
a symbol, put it into res set, sum up all values in the res set and return the answer

part 1: 546563
part 2: 91031374


'''
from collections import defaultdict

def search(graph, R, C, start_x, start_y):
  # search each adjacent direction
  direction = [(-1,0), (1,0),
              (0,-1), (0,1),
              (1,-1), (-1,1),
              (-1,-1), (1,1)
              ]

  # searching in each direction for each coordinate pair
  for x, y in direction:
    if 0 <= start_x+x < R and 0 <= start_y+y < C and not graph[start_x+x][start_y+y].isdigit()  and graph[start_x+x][start_y+y] != '.':
      return True
  
  return False

def question_one():
  with open("day3.txt") as f:
      lines = f.read().split("\n")

  grid = [[char for char in line] for line in lines]
  ROWS_LEN = len(grid)
  COLS_LEN = len(grid[0])

  res = 0

  for curr_r in range(ROWS_LEN):
    curr_num = 0
    is_part = False
    # plus 1 to catch last column and not skip it since its not inclusive
    for curr_col in range(COLS_LEN+1):
      if curr_col < COLS_LEN and grid[curr_r][curr_col].isdigit():
        curr_num = curr_num*10 + int(grid[curr_r][curr_col])
        if search(grid, ROWS_LEN, COLS_LEN, curr_r, curr_col):
          is_part = True
      # if curr index is not a number and we have itereated through a num we add this to res
      elif curr_num > 0:
        if is_part:
          res += curr_num
        curr_num = 0
        is_part = False
      
  print(res)


def question_two():
  with open("day3.txt") as f:
      lines = f.read().split("\n")

  grid = [[char for char in line] for line in lines]
  ROWS_LEN = len(grid)
  COLS_LEN = len(grid[0])

  res = 0
  # map of parts that share the same gear r,c 
  gears_map = defaultdict(list)
  for curr_r in range(ROWS_LEN):
    # set so u dont keep adding to the same r,c value from the same number
    gears_set = set()
    curr_num = 0
    # plus 1 to catch last column and not skip it since its not inclusive
    for curr_col in range(COLS_LEN+1):
      if curr_col < COLS_LEN and grid[curr_r][curr_col].isdigit():
        curr_num = curr_num*10 + int(grid[curr_r][curr_col])
        # searching in each direction for each coordinate pair
        for x, y in [(-1,0), (1,0),
            (0,-1), (0,1),
            (1,-1), (-1,1),
            (-1,-1), (1,1)
            ]:

          if 0<=curr_r+x<ROWS_LEN and 0 <=curr_col + y < COLS_LEN and grid[curr_r+x][curr_col + y] == "*":
          # add it to the set of gears
            gears_set.add((curr_r+x, curr_col + y))
      # if curr index is not a number and we have itereated through a num we add this to res
      elif curr_num > 0:
        # if this number belongs to multiple gear sets
        for gear in gears_set:
          gears_map[gear].append(curr_num)
        curr_num = 0
        gears_set= set()


  # sum up the product of each part
  for k,v in gears_map.items():
    if len(v) == 2:
      res += v[0] * v[1]
      
  print(res)


question_one()
question_two()
