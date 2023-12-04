# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

arr = [ 1, 1, 1, 2, 1, 1 ]
arr = sorted(arr)

print(f"{arr}")

def find_uniq(arr):
    # your code here

    arr = sorted(arr)
    if arr[0] == arr[1]:
        return arr[-1]
    
    return arr[0]   # n: unique number in the array

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))