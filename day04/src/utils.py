def split_input(input):
    _, cards = input.split(":")
    key, nums = cards.split("|")
    key = key.split()
    nums = nums.split()
    return key, nums

def check_winners(key, nums):
    double = 0
    for num in nums:
        if num in key:
            if double == 0:
                double = 1
            else:
                double *= 2
    return double