'''Given an array of integers your solution should find the smallest integer.
For example:
Given [1, 2, 3, 4] your solution will return 1'''

def find_small_num(arr):
    return sorted(arr)[0]

print(find_small_num([1, 2, 3, 4]))