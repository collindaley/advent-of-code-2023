import os
from utils import seperate_input, is_game_possible, least_possible_cubes

filename = os.path.join(os.getcwd(), 'day02', 'data', 'input.txt')
with open(filename, 'r') as file:
    inputs = file.readlines()

part1 = 0
part2 = 0
for i in range (0, len(inputs)):
    game = seperate_input(inputs[i])
    if is_game_possible(12, 13, 14, game):
        part1 += i + 1
    part2 += least_possible_cubes(game)

print(part1)
print(part2)

