'''
1681758908
803
'''

# extend this to do it for every line 
# test = "0 3 6 9 12 15"
def calculate_next(vals):
  # base case
  if all(x == 0 for x in vals):
    return 0

  #  zip allows you to pairwise quickly
  diffs = [y-x for x,y in zip(vals, vals[1:])]
  last_elem = calculate_next(diffs)
  return last_elem + vals[-1]


def calculate_next_reverse(vals):
  vals = vals[::-1]
  # base case
  if all(x == 0 for x in vals):
    return 0

  diffs = [y-x for x,y in zip(vals, vals[1:])]
  last_elem = calculate_next(diffs)
  return last_elem + vals[-1]


l = [[int(i) for i in s.split()] for s in open('day9.txt').read().split('\n') if s.strip()]

res = 0
res2 = 0

for line in l:

  res += calculate_next(line)
  res2+= calculate_next_reverse(line)
print(res, res2)




