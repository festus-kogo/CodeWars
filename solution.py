# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

# Reversed Strings


# Complete the solution so that it reverses the string passed into it.

    # 'world'  =>  'dlrow'
    # 'word'   =>  'drow'

string = "world"
string_list = list(string)
print(string_list)

count = len(string_list)

i = 1

arr = []

while i <= count:
    # print(i)
    item_pos = -abs(i)
    arr.append(string_list[item_pos])
    i += 1

print(arr)
print("".join(arr))

def solution(string):
    # pass
    string_list = list(string)
    print(string_list)

    count = len(string_list)

    i = 1

    arr = []

    while i <= count:
        item_pos = -abs(i)
        arr.append(string_list[item_pos])
        i += 1
    
    return "".join(arr)