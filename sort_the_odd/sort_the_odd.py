# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    odd_list = [x for x in source_array if x % 2 != 0]
    sorted_odd_list = sorted(odd_list)

    even_nums_dict = {i: x for i, x in enumerate(source_array) if x % 2 == 0}

    for k, v in even_nums_dict.items():
        sorted_odd_list.insert(k, v)

    return sorted_odd_list

print(f"{sort_array([5, 3, 2, 8, 1, 4])}")
# [1, 3, 2, 8, 5, 4]
# [1, 3, 2, 8, 5, 4]

print(f"{sort_array([5, 3, 1, 8, 0])}")
# [1, 3, 5, 8, 0]
# [1, 3, 5, 8, 0]

print(f"{sort_array([5, 3, 2, 8, 1, 4, 11])}")
# [1, 3, 2, 8, 5, 4, 11]
# [1, 3, 2, 8, 5, 4, 11]

print(f"{sort_array([2, 22, 37, 11, 4, 1, 5, 0])}")
# [2, 22, 1, 5, 4, 11, 37, 0]
# [2, 22, 1, 5, 4, 11, 37, 0]


