# https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python

import string

def name_value(my_list):
  letters = string.ascii_lowercase
  result = []

  for i, k in enumerate(my_list):
    i_without_space = k.replace(" ", "")
    item_index = i + 1
    total = 0

    for j in i_without_space:
        total += letters.index(j) + 1
    
    result.append(total * item_index) 

  return result

print(f"{name_value(['abc'])}") # [6]
print(name_value(["codewars","abc","xyz"])) # [88, 12, 225]
print(name_value(["abc abc","abc abc","abc","abc"]))
print(f"{name_value(['abc', 'abc abc'])}")# [6, 24]