# Array.diff
# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python


def array_diff(a, b):
    result = []

    for i in a:
        print(f"{i}")
        if i not in b:
            result.append(i)
    
    return result

print(array_diff([1,2], [1])) # [2]
print(array_diff([1,2,2], [1])) # [2, 2]
print(array_diff([1,2,2], [2])) # [1]
print([1,2,2], []) # []
print(array_diff([], [1,2])) # []
print(array_diff([1,2,3], [1, 2])) # [3]