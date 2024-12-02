import re
from string import digits

def question_one():
    # Using readline()
    file1 = open('day1.txt', 'r')
    sum_vals = 0

    while True:
        # Get next line from file
        line = file1.readline()
    
        # if line is empty
        # end of file is reached
        if not line:
            break

        nums = re.findall(r'\d+',line)
        vals = "".join(nums)
        val = int(vals[0] + vals[-1])
        sum_vals += val
    
    print(sum_vals)


def question_two():
    with open("day1.txt") as f:
        lines = f.read().split("\n")

    res = 0
    nums_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in lines:
        numbers = []
        for d in digits:
            idx = line.find(d)
            if idx != -1:
                numbers.append((idx, d))
            idx = line.rfind(d)
        for key, val in nums_dict.items():
            idx = line.find(key)
            if idx != -1:
                numbers.append((idx, val))
            idx = line.rfind(key)

        numbers.sort()
        res += int(f"{numbers[0][1]}{numbers[-1][1]}")

    print(res)

question_one()
question_two()