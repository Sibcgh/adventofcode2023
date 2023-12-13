#  lets try a naive brute force method initally
from functools import cache

'''
8193
45322533163795
'''

# backtracking function to generate all possible options
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

# wallahi shout out to cashing
@cache
def count(curr_obj, sequence, flag=False):
  if curr_obj == "":
    return 1 if sum(sequence) == 0 else 0

  if sum(sequence) == 0:
    return 0 if "#" in curr_obj else 1
  
  if curr_obj[0] == "#":
    if flag and sequence[0] == 0:
      return 0
    return count(curr_obj[1:], (sequence[0] - 1, *sequence[1:]), True)
  
  if curr_obj[0] == ".":
    if flag and sequence[0] > 0:
      return 0
    return count(curr_obj[1:], sequence[1:] if sequence[0] == 0 else sequence, False)
  
  if flag:
    if sequence[0] == 0:
      return count(curr_obj[1:], sequence[1:], False)
    return count(curr_obj[1:], (sequence[0] - 1, *sequence[1:]), True)
  
  return count(curr_obj[1:], sequence, False) + count(curr_obj[1:], (sequence[0] - 1, *sequence[1:]), True)

# def question_one_brute_force():
#   res = 0

#   for line in open("day12.txt"):
#       pattern, sequence = line.split()
#       # sequence = tuple(map(int, sequence.split(",")))
#       sequence = [int(num) for num in sequence.split(",")]
#       combinations = find_patterns(pattern)

#       for combo in combinations:
#         seq = [len(seq) for seq in combo.split(".") if seq]
#         if seq == sequence:
#             res+=1

#   print(res)

def question_one():
  res = 0

  for line in open("day12.txt"):
      pattern, sequence = line.split()
      sequence = tuple(map(int, sequence.split(",")))
      res += count(pattern, sequence)
  print(res)

def question_two():
  res = 0

  for line in open("day12.txt"):
      pattern, sequence = line.split()
      sequence = tuple(map(int, sequence.split(",")))
      pattern = "?".join([pattern] * 5)
      sequence *= 5
      res += count(pattern, sequence)

  print(res)

question_one()
question_two()
