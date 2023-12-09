import os
from utils import split_input, check_winners

# input file
filename = os.path.join(os.getcwd(), 'day04', 'data', 'input.txt')
with open(filename, 'r') as file:
    inputs = file.readlines()

part1 = 0
for input in inputs:
    key, nums = split_input(input)
    
    part1 += check_winners(key, nums)

print(part1)