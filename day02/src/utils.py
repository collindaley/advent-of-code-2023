import re

def seperate_input(input):
    _, games = input.split(":")
    games = games.split(";")
    
    output = []

    for game in games:
        output.append(re.findall("(\d+) (red|green|blue)", game))

    return output

def is_game_possible(red, green, blue, hands):
    for hand in hands:
        for color in hand:
            match color[1]:
                case "red":
                    if int(color[0]) > red:
                        return False
                case "green":
                    if int(color[0]) > green:
                        return False
                case "blue":
                    if int(color[0]) > blue:
                        return False
                case _:
                    break
    return True

def least_possible_cubes(hands):
    red, green, blue = 0, 0, 0
    for hand in hands:
        for color in hand:
            match color[1]:
                case "red":
                    if int(color[0]) > red:
                        red = int(color[0])
                case "green":
                    if int(color[0]) > green:
                        green = int(color[0])
                case "blue":
                    if int(color[0]) > blue:
                        blue = int(color[0])
                case _:
                    break
    return red * green * blue