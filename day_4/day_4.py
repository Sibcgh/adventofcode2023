'''
Note:
Use test input and create my own as well to cover edge cases that could be in the general input

#  iterate line by line, 
seperate each line by : then by |,
first slice is winning nums, second slice is curr nums
count up all winning nums in curr nums,
return 2^(count-1)

test 
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

'''
from collections import defaultdict

def card_points(input_text):
  first_split = input_text.split(":")

  second_split = first_split[1].split("|")
  winning_nums = [int(s) for s in second_split[0].split() if s.isdigit()]
  curr_nums = [int(s) for s in second_split[1].split() if s.isdigit()]

  count = 0
  for num in curr_nums:
    if num in winning_nums:
      count+=1

  if count > 0:
    count = 2**(count -1)
  else:
    count = 0
  return count


def scratchcards(input_text):
  first_split = input_text.split(":")
  second_split = first_split[1].split("|")
  winning_nums = [int(s) for s in second_split[0].split() if s.isdigit()]
  curr_nums = [int(s) for s in second_split[1].split() if s.isdigit()]

  count = 0
  for num in curr_nums:
    if num in winning_nums:
      count+=1
  return (count)

def question_one():
  with open("day4.txt") as f:
      lines = f.read().split("\n")

  res = 0

  for line in lines:
    line = line.strip()
    res += card_points(line)

  print(res)


def question_two():
  with open("day4.txt") as f:
      lines = f.read().split("\n")

  res = 0
  cards = defaultdict(int)

  for i,line in enumerate(lines):
    cards[i] += 1
    line = line.strip()
    count = scratchcards(line)
    for curr in range(count):
      cards[i+1+curr] += cards[i]

  res = (sum(cards.values()))
  print(res)


question_one()
question_two()