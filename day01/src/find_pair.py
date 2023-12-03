import re

def find_pair(input):
    first = re.search(r'(\d)', input).group()
    last = re.search(r'\d(?=\D*$)', input).group()
    return int(first + last)