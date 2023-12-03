import os
from find_pair import find_pair

total = 0
filename = os.path.join(os.getcwd(), 'day01', 'data', 'input.txt')
with open(filename, 'r') as file:
    inputs = file.readlines()

for input in inputs:
    total += find_pair(input)

print(total)