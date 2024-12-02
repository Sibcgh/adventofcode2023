'''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

extremely hard question, you can probably count this as a leetcode hard ++ takes over an hour to do
'''

def question_one():
  with open("day5.txt") as f:
      seeds, *chunks = f.read().split('\n\n')

  # initalize all the seed values
  seeds = list(int(s) for s in seeds.strip().split()[1:])

  # each chunk is a map 
  #  we are getting each tuple dest, src, range_len and then 
  # iterating over the seeds array to map them to their new 
  # destination value without creating a new map 
  for chunk in chunks:
    ranges = []
    for line in chunk.splitlines()[1:]:
      # vals = [int(s) for s in line.split() if s.isdigit()]
      #  ^ slower way than doing the bottom 
      ranges.append(list(map(int, line.split())))

    # updated seed values
    new_seeds = []
    
    for curr in seeds:
      for dest, source, range_len in ranges:
        # if current seed in the range then we can add it to the new seed array
        if curr in range(source, source + range_len):
          # seed value is adjusted with the offset
          new_seeds.append(curr + dest - source)
          break
      else:
        # for else means if the loop didnt break, meaning we break if the curr seed doesnt have a mapping in the tuple
        # if we dont find a match we just add in the original seed value
        # it just means there is no offset and we add in the original seed value
        new_seeds.append(curr)
      #  update the array with the new value from the chunk
      seeds = new_seeds

  # print the minimum value from the last array 
  print(min(seeds))

def question_two():
	with open("day5.txt") as f:
		inputs, *chunks = f.read().split('\n\n')

	inputs = list(int(s) for s in inputs.strip().split()[1:])

	# initalize all the seed values
	seeds = []

	# create a tuple of seeds containing start and end indices
	for i in range(0, len(inputs), 2):
		seeds.append((inputs[i], inputs[i] + inputs[i+1]))
	
	for chunk in chunks:
		ranges = []
		for line in chunk.splitlines()[1:]:
			ranges.append(list(map(int, line.split())))
		new_seeds = []
		# iterate through updating all the seed intervals
		while len(seeds) > 0:
			# start and end interval of seed
			start, end = seeds.pop()
			#  end interval, start interval and range from beginning to start for new tuple
			for a, b, c in ranges:
				# start will be the max of the starting values of the intervals
				os = max(start, b)
				# end will be the minimum value of the 2 intervals
				oe = min(end, b + c)
				# if there is no overlap between the overlap start and overlap end value we can add into the new seed array
				if os < oe:
					# add in new seeds from overlap start to offset diff between dest and start value
					new_seeds.append((os - b + a, oe - b + a))
					# overlapping between the starting values
					if os > start:
						seeds.append((start, os))
					if end > oe:
						# overlapping between ending values
						seeds.append((oe, end))
					break
			else:
				# no mapping for seed interval in the new tuple just add old mapping 
				new_seeds.append((start, end))

		#  update the array with the new value from the chunk
		seeds = new_seeds

	#  no need to merge intervals because if we sort we will only need to rely on the smallest leftside interval value
	print(sorted(seeds)[0][0])

question_one()
question_two()

