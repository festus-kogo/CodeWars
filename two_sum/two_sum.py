# https://www.codewars.com/kata/52c31f8e6605bcc646000082/python

def two_sum(numbers, target):

    for i, element_i in enumerate(numbers):
        for j, element_j in enumerate(numbers):
            if i != j and element_i + element_j == target:
                return [i, j]

print(two_sum([1, 2, 3], 4)) # [0, 2]
print(two_sum([1234,5678,9012], 14690)) # [1, 2]
print(two_sum([2,2,3], 4)) # [0, 1]
print(f"{two_sum([3,0,27,11,16,13,17,19,6,26,2,3], 43)}") # [2, 4, 6, 9]
print(f"{two_sum([28,0,21,6,14,12,15,23,8,11], 27)}") # [2, 3, 5, 6]
print(f"{two_sum([9,22,3,20,15,21,25,20], 40)}") # [3, 4, 6, 7]