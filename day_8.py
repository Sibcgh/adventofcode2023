from collections import defaultdict
import re
import math

def question_one():
  with open("day8.txt") as f:
    inputs = f.read().split('\n\n')

    chunks = inputs[1].split('\n')

    graph = defaultdict(list)
    instructions = []
    directions = inputs[0]


    for step in directions:
      instructions.append(step) 

    # for each line convert to graph
    for line in chunks:
      s,r,l = re.findall(r'(\w+)',line)
      graph[s].append((r,l))

    # start at AAA
    next_node = "AAA"
    steps = 0

    while next_node != "ZZZ":
      next_dir = instructions.pop(0)
      instructions.append(next_dir)
      steps += 1

      # if left check 0th node
      if next_dir == "L":
        next_node =  graph[next_node][0][0]
      else:
        next_node =  graph[next_node][0][1]

    print(steps)

def question_two():
  with open("day8.txt") as f:
    inputs = f.read().split('\n\n')

    chunks = inputs[1].split('\n')

    graph = defaultdict(list)
    instructions = []
    directions = inputs[0]
    for step in directions:
      instructions.append(step) 

    # for each line convert to graph
    for line in chunks:
      s,r,l = re.findall(r'(\w+)',line)
      graph[s].append((r,l))

    start_positions  = [node for node in graph if node.endswith("A")]
    cycles = []

    for current in start_positions:
        cycle = []

        current_steps = instructions
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current.endswith("Z"):
              next_dir = instructions.pop(0)
              instructions.append(next_dir)
              step_count += 1

              # if left check 0th node
              if next_dir == "L":
                current =  graph[current][0][0]
              else:
                current =  graph[current][0][1]


            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]

    res = math.lcm(*nums)
    print(res)
        
# question_one()
question_two()
