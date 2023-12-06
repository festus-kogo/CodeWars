# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def sum_of_three(arr):
    _sum = 0

    for i in arr:
        _sum += i

    return _sum

def tribonacci(signature, n):
    _len = len(signature)

    if n == 0:
        return []
    elif n == 1:
        return signature[:1]
    elif n == 2:
        return signature[:2]
    
    while _len < n:
        _sum_of_three = sum_of_three(signature[-3:])
        signature.append(_sum_of_three)
        _len += 1
    return signature

print(tribonacci([144, 14, 118], 1)) # [156, 70]
print(tribonacci([156, 70, 139], 2)) # [156, 70]
print(tribonacci([159, 179, 18], 2)) # [159, 179]
print(tribonacci([51, 55, 127], 2)) # [51, 55]
# print(tribonacci([1, 1, 1], 10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
# print(tribonacci([0, 0, 1], 10)) # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
# print(tribonacci([0, 1, 1], 10)) # [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
# print(tribonacci([1, 0, 0], 10)) # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
# print(tribonacci([0, 0, 0], 10)) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(tribonacci([1, 2, 3], 10)) # [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
# print(tribonacci([3, 2, 1], 10)) # [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
# print(tribonacci([1, 1, 1], 1)) # [1, 1, 1]
# print(tribonacci([300, 200, 100], 0)) # []
# print(tribonacci([0.5, 0.5, 0.5], 30)) # [1]
