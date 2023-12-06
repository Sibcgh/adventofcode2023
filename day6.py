
'''
janky brute force soln
'''


def question_one():
  with open("day6.txt") as f:
    lines = f.read().split('\n')

  times = list(int(s) for s in lines[0].strip().split()[1:])
  distances = list(int(s) for s in lines[1].strip().split()[1:])

  nums = []

  for i in range(len(times)):
    count = 0
    for j in range(1,times[i]):
      speed = times[i] - j 
      new_dist = j * speed
      if new_dist > distances[i]:
        count +=1
    nums.append(count)


  res = 1
  for count in nums:
    res *= count

  print(res)


def question_two():
  with open("day6.txt") as f:
    lines = f.read().split('\n')

  times = list((s) for s in lines[0].strip().split()[1:])
  distances = list((s) for s in lines[1].strip().split()[1:])

  times_ = int("".join(times))
  distances_ = int("".join(distances))

  nums = []

  count = 0
  for j in range(1,times_):
    speed = times_ - j 
    new_dist = j * speed
    if new_dist > distances_:
      count +=1


  print(count)

question_one()

question_two()