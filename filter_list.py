# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
# List Filtering

# my_list = [1,2,'a','b']
# my_list = [1,'a','b',0,15]
# my_list = [1,2,'aasf','1','123',123]
# arr = []

# for element in my_list:
#     # print(type(element))
#     if type(element) == str:
#         continue

#     arr.append(element)

# print(arr)

def filter_list(l):
    arr = []

    for element in l:
        if type(element) == str:
            continue

        arr.append(element)
    # 'return a new list with the strings filtered out'
    return arr

print(filter_list([1, 2, 'a', 'b'])) # [1, 2]
print(filter_list([1, 'a', 'b', 0, 15])) # [1, 0, 15]
print(filter_list([1, 2, 'aasf', '1', '123', 123])) # [1, 2, 123]
