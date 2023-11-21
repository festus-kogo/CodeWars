# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
# Count by X

# x = 1
# n = 10

# x = 2
# n = 5

# x = 1
# n = 5
# for i in range(x, (x * n + 1), x):
#     print(i)

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    arr = []

    for i in range(x, (x * n + 1), x):
        # print(i)
        arr.append(i)

    return arr

print(count_by(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_by(2,5)) # [2, 4, 6, 8, 10]
print(count_by(1, 5)) # [1, 2, 3, 4, 5]