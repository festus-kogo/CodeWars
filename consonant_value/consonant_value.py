# https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

import string

def solve(s):
    letters = string.ascii_lowercase
    vowels = "aeiou"
    values = []
    vowels_replaced = s

    for i, j in enumerate(vowels):
        if j in vowels_replaced:
            # print(f"found {j} in {vowels}")
            vowels_replaced = vowels_replaced.replace(j, " ")

    lst = vowels_replaced.split() # ['z', 'd', 'cs']

    for x in lst:
        # print(f"{x}")
        total = 0
        for y in x:
            # print(f"{y}")
            total += letters.index(y) + 1
        values.append(total)

    return max(values)

print(solve("zodiacs")) # 26
print(solve("strength")) # 57
print(solve("cozy")) # 51
print(solve("xyzzy")) # 126
print(solve("zodiac")) # 26
print(solve("chruschtschov")) # 80
print(solve("khrushchev")) # 38
print(solve("catchphrase")) # 73
print(solve("twelfthstreet")) # 103