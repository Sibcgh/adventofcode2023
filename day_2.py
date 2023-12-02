'''
Initially create a global counter for red, green and blue balls 

go line by line and check to see if in each game state
first seperate by : to get game number 
then seperate on ; to get each iteration
go through each iteration, get count and color
put into a counter, compare if each counter value is less than or equal to gobal counter
if u find one that breaks the global counter, break and go to next game state
if not continue until you read the whole line and then add game number to global counter


bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
'''
from collections import Counter

global_counter = Counter()
global_counter['blue'] = 14
global_counter['green'] = 13
global_counter['red'] = 12


def check_inputs(input_text):
  # first split to get game ID
  first_split = input_text.split(":")

  gameId = [int(s) for s in first_split[0].split() if s.isdigit()].pop()
  curr_game_valid = True
  # second split to get each pick
  second_split = first_split[1].split(";")

  for instance in second_split:
    if not curr_game_valid:
      break

    # third split to get each color and color and num
    third_split = instance.split(",")
    color_counter = Counter()
    for option in third_split:
      indx = option.find('blue')
      if indx != -1:
        color_counter['blue'] = [int(s) for s in option.split() if s.isdigit()].pop()

      indx = option.find('red')
      if indx != -1:
        color_counter['red'] = [int(s) for s in option.split() if s.isdigit()].pop()

      indx = option.find('green')
      if indx != -1:
        color_counter['green'] = [int(s) for s in option.split() if s.isdigit()].pop()

    for color in color_counter:
      if color_counter[color] > global_counter[color]:
        curr_game_valid = False
        break

  # if we itereated completely through and no breaks we can append this gameID to res
  return gameId if curr_game_valid else 0

def check_inputs_min_power(input_text):
  # first split to get game ID
  first_split = input_text.split(":")

  # second split to get each pick
  second_split = first_split[1].split(";")

  min_green = 0
  min_red = 0
  min_blue = 0

  for instance in second_split:
    # third split to get each color and color and num
    third_split = instance.split(",")
    color_counter = Counter()
    for option in third_split:
      indx = option.find('blue')
      if indx != -1:
        color_counter['blue'] = [int(s) for s in option.split() if s.isdigit()].pop()

      indx = option.find('red')
      if indx != -1:
        color_counter['red'] = [int(s) for s in option.split() if s.isdigit()].pop()

      indx = option.find('green')
      if indx != -1:
        color_counter['green'] = [int(s) for s in option.split() if s.isdigit()].pop()

    #  change to find min value for ball color 
    for color in color_counter:
        if color == 'green':
          min_green = max(color_counter[color] , min_green)
        if color == 'red':
          min_red = max(color_counter[color] , min_red)
        if color == 'blue':
          min_blue = max(color_counter[color] , min_blue)


  # return power of min of all colours
  return min_green * min_red * min_blue

def question_one():
  with open("day2.txt") as f:
      lines = f.read().split("\n")

  res = 0

  for line in lines:
    line = line.strip()
    res += check_inputs(line)

  print(res)

def question_two():
  with open("day2.txt") as f:
      lines = f.read().split("\n")

  res = 0

  for line in lines:
    line = line.strip()
    res += check_inputs_min_power(line)

  print(res)

question_one()
question_two()


