
'''
janky brute force soln
'''
from math import prod

def question_one_brute_force(lines):
  times = list(int(s) for s in lines[0].strip().split()[1:])
  distances = list(int(s) for s in lines[1].strip().split()[1:])

  nums = []

  for i in range(len(times)):
    count = 0
    for j in range(1,times[i]):
      if (times[i] - j ) * j > distances[i]:
        count +=1
    nums.append(count)


  res = 1
  res = prod(nums)
  print(res)


def question_two_brute_force(lines):
  times = list((s) for s in lines[0].strip().split()[1:])
  distances = list((s) for s in lines[1].strip().split()[1:])

  times_ = int("".join(times))
  distances_ = int("".join(distances))

  nums = []

  count = 0
  for j in range(1,times_):
    if (times_ - j ) * j  > distances_:
      count +=1


  print(count)



with open("day6.txt") as f:
  inputs = f.read().split('\n')


question_one_brute_force(inputs)
question_two_brute_force(inputs)