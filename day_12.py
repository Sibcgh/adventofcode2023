#  lets try a naive brute force method initally
import functools

# backtracking function to generate all possible options
@functools.lru_cache(maxsize=None)
def find_patterns(pattern):
  def backtrack(index, path):
    if index == len(pattern):
      combinations.append("".join(path))
      return

    curr_char = pattern[index]
    # do backtracking options
    if  curr_char == "?":
      for char in "#.":
        path.append(char)
        backtrack(index + 1, path)
        path.pop()
    else:
      path.append(curr_char)
      backtrack(index +1, path)
      path.pop()
  
  
  combinations = []
  backtrack(0, [])
  return combinations


def question_one():
  with open("day12.txt") as f:
    lines = f.read().split('\n')

    res = 0

    for line in lines:
      line = line.split()
      pattern = line[0]
      sequence = [int(num) for num in line[1].split(",")]

      combinations = find_patterns(pattern)

      for combo in combinations:
          seq = [len(seq) for seq in combo.split(".") if seq]
          if seq == sequence:
            res += 1

  print(res)

'''
  ???.### 1,1,3
 
  ???.###????.###????.###????.###????.###
 '''

def question_two():
  with open("day12.txt") as f:
    lines = f.read().split('\n')

    res = 0

    for line in lines:
      line = line.split()
      pattern = line[0]

      curr = ""
      for j in range(5):
          curr+= "?"
          curr += pattern
      sequence = [int(num) for num in line[1].split(",")]
      sequence = sequence * 5

      print(curr[1:], sequence)
      combinations = find_patterns(curr[1:])

      for combo in combinations:
          seq = [len(seq) for seq in combo.split(".") if seq]
          if seq == sequence:
            res += 1

  print(res)


# question_one()
question_two()