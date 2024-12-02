with open("day15.txt") as f:
    step = f.read().split(',')

res = 0

for part in step:
    curr = 0
    for char in part:
        curr += ord(char)
        curr *= 17
        curr %= 256
    res += curr

print(res)