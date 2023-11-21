# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
# Find the stray number

l = [1, 1, 2]

# print(sorted(l))

def stray(arr):
    # pass'
    arr = sorted(arr)
    if len(arr) >= 3:
        # pass
        for element in arr:
            if element != arr[0] or element != arr[1]:
                return element

    else:
        print(f"{arr} length does not pass the test!")

print(stray([1, 1, 3])) # 3
print(stray([17, 17, 3, 17, 17, 17, 17])) # 3
print(stray([17, 17, 4, 17, 17, 17, 17])) # 4
print(stray([1, 1, 1, 1, 1, 1, 2])) # 2
print(stray([2, 3, 2, 2, 2])) # 3
print(stray([3, 2, 2, 2, 2])) # 3