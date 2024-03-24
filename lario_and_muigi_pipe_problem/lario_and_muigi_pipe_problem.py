# https://www.codewars.com/kata/56b29582461215098d00000f/train/python

def pipe_fix(nums):
    return [x for x in range(nums[0], (nums[-1] + 1), 1)]

print(f"{pipe_fix([1, 2, 3, 5, 6, 8, 9])}") # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{pipe_fix([1, 3, 5, 6, 7, 8])}") # [1, 2, 3, 4, 5, 6, 7, 8]
print(f"{pipe_fix([1, 2, 3, 12])}") # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]