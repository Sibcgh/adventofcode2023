'''
1681758908
803
'''

# extend this to do it for every line 
# test = "0 3 6 9 12 15"
def calculate_next(input_text):
  vals = list(int(s) for s in input_text.strip().split())


  diffs = [vals]

  curr_arr = vals

  while True:
    curr_diffs = []

    for i in range(1, len(curr_arr)):
      curr_diffs.append(curr_arr[i]- curr_arr[i-1])
    diffs.append(curr_diffs)
    curr_arr = curr_diffs


    if sum(curr_arr) == 0:
      break


  # iterate backwards, pop off the last element and set it to curr num


  last_elem = 0

  while diffs:
    curr_arr = diffs[-1]
    curr_num = curr_arr[-1]
    last_elem = last_elem + curr_num
    diffs.pop()

  return(last_elem)

def calculate_next_reverse(input_text):
  vals = list(int(s) for s in input_text.strip().split())
  vals = vals[::-1]

  diffs = [vals]

  curr_arr = vals

  while True:
    curr_diffs = []

    for i in range(1, len(curr_arr)):
      curr_diffs.append(curr_arr[i]- curr_arr[i-1])
    diffs.append(curr_diffs)
    curr_arr = curr_diffs


    if sum(curr_arr) == 0:
      break


  # iterate backwards, pop off the last element and set it to curr num


  last_elem = 0

  while diffs:
    curr_arr = diffs[-1]
    curr_num = curr_arr[-1]
    last_elem = last_elem + curr_num
    diffs.pop()

  return(last_elem)

res = 0
res2 = 0

with open("day9.txt") as f:
  lines = f.read().split('\n')


for line in lines:

  res += calculate_next(line)
  res2+= calculate_next_reverse(line)
print(res, res2)
