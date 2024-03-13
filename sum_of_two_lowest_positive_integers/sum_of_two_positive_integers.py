# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    #your code here
    return sorted(numbers)[0] + sorted(numbers)[1]

print(sum_two_smallest_numbers([5, 8, 12, 18, 22])) # 13
print(sum_two_smallest_numbers([7, 15, 12, 18, 22])) # 19
print(sum_two_smallest_numbers([25, 42, 12, 18, 22])) # 30
print(sum_two_smallest_numbers([19, 5, 42, 2, 77])) # 7
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])) # 3453455
