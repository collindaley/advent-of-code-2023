import re

def find_nums(arr, index):
    sum = 0
    regex = re.compile("\d+")
    for match in re.finditer(regex, arr):
        if any(index-1 <= value <= index+1 for value in range(match.start(),match.end())):
            sum += int(match.group())
            arr = arr[:match.start()] + "." * len(match.group()) + arr[match.end():]
    return arr, sum
