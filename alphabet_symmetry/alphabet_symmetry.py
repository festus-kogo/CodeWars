# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python

import string

def solve(strings : list[str]) -> list[int]:
    alphabet = string.ascii_lowercase    
    outer_arr = []

    for i in strings:
        inner_arr = []
        
        for j, x in enumerate(i.lower()):
            if j + 1 == alphabet.index(x) + 1:
                inner_arr.append(x)

        outer_arr.append(len(inner_arr))
    return outer_arr

print(solve(["abode","ABc","xyzD"]))
print(solve(["abide","ABc","xyz"]))
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]))
print(solve(["encode","abc","xyzD","ABmD"]))