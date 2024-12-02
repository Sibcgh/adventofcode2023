def question_one(empty_rows, empty_cols, galaxies):
  # dont manipulate the grid directly
  res = 0
  factor = 2
  for indx, (r1,c1) in enumerate(galaxies):
    for (r2, c2) in galaxies[:indx]:
      # cant do chebyshov distance directly because of hte gravity issue
      #  iterate over row and col from min to max to keep searching consistent
      for r in range(min(r1, r2), max(r1, r2)):
        if r in empty_rows: 
          res += factor 
        else:
          res +=1
      for c in range(min(c1, c2), max(c1, c2)):
        if c in empty_cols: 
          res += factor 
        else:
          res +=1

  print(res)


def question_two(empty_rows, empty_cols, galaxies):
  # dont manipulate the grid directly
  res = 0
  factor = 1000000
  for indx, (r1,c1) in enumerate(galaxies):
    for (r2, c2) in galaxies[:indx]:
      # cant do chebyshov distance directly because of hte gravity issue
      #  iterate over row and col from min to max to keep searching consistent
      for r in range(min(r1, r2), max(r1, r2)):
        if r in empty_rows: 
          res += factor 
        else:
          res +=1
      for c in range(min(c1, c2), max(c1, c2)):
        if c in empty_cols: 
          res += factor 
        else:
          res +=1

  print(res)


with open("day11.txt") as f:
  grid = f.read().splitlines()

empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
# similar to how to transpose a matrix 
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]
galaxies = [(r,c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == '#']


question_one(empty_rows=empty_rows, empty_cols=empty_cols, galaxies=galaxies)
question_two(empty_rows=empty_rows, empty_cols=empty_cols, galaxies=galaxies)