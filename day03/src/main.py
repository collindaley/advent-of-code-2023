import re
import os
from utils import find_nums

# input file
filename = os.path.join(os.getcwd(), 'day03', 'data', 'input.txt')
with open(filename, 'r') as file:
    input = file.readlines()

# strip lines of \n
for i in range(len(input)):
    input[i] = input[i].strip()

regex = re.compile("[^A-Za-z0-9\.]")
part1 = 0

# Find all part numbers
for i in range(len(input)):
    for match in re.finditer(regex, input[i]):
        for j in range(match.start(), match.end()):
            if i > 0:
                input[i-1], a = find_nums(input[i-1],j)
                part1 += a
            input[i], b = find_nums(input[i],j)
            part1 += b
            if i < len(input):
                input[i+1], c = find_nums(input[i+1],j)
                part1 += c

print(part1)