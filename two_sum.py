# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
# Two Sum

my_list = [1, 2, 3]
my_target = 4
arr = []

# for i in my_list:
#     for j in my_list:
# 		# print(j)
#         if my_list.index(i) == my_list.index(j):
#             continue
#         else:
#             sum = i + j
#             if sum == my_target:
#                   arr.append(my_list.index(i))
#                 #   arr.append(my_list.index(j))
                  
# print(arr)

###############################################################
def two_sum(numbers, target):
    arr = []
    # my_sum = 0

    for i in numbers:
        for j in numbers:
            if numbers.index(i) == numbers.index(j):
                continue # Skip the element at this index
            else:
                my_sum = i + j
                if my_sum == target:
                    arr.append(numbers.index(i))
                    # arr.append(numbers.index(j))
    return arr

def two_sum1(numbers, target):
    arr = []

    for i, element_i in enumerate(numbers):
        for j, element_j in enumerate(numbers):
            if i == j:
                continue # Skip the element at this index
            else:
                my_sum = element_i + element_j
                if my_sum == target:
                    arr.append(i)
                    # arr.append(numbers.index(j))
    return arr

# print(two_sum([1, 2, 3], 4)) # [0, 2]
# print(two_sum([1234,5678,9012], 14690)) # [1, 2]
# print(two_sum([2,2,3], 4)) # 

print(two_sum1([1, 2, 3], 4)) # [0, 2]
print(two_sum1([1234,5678,9012], 14690)) # [1, 2]
print(two_sum1([2,2,3], 4)) # [0, 1]