# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python

def flatten_and_sort(array):
    ar = []

    if array == []:
        return []

    for i in array:
        for j in i:
            ar.append(j)

    return sorted(ar)