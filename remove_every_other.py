# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python
# Removing Elements

# l = ['Hello', 'Goodbye', 'Hello Again']
# print(l)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list = [[1, 2]]
# my_list = ['Hello', 'Goodbye', 'Hello Again']
# my_list = [['Goodbye'], {'Great': 'Job'}]

# arr = []
# for i, j in enumerate(my_list):
#     # print(i, j)
#     if i % 2 == 0:
#         # print(i, j)
#         arr.append(j)
# print(arr)

def remove_every_other(my_list):
    # Your code here!
    # pass
    arr = []
    for i, j in enumerate(my_list):
        # print(i, j)
        if i % 2 == 0:
            # print(i, j)
            arr.append(j)
    return arr

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again'])) # ['Hello', 'Hello Again']
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1, 3, 5, 7, 9]
print(remove_every_other([[1, 2]])) # [[1, 2]]
print(remove_every_other([['Goodbye'], {'Great': 'Job'}])) # [['Goodbye']]