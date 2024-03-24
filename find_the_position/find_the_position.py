# https://www.codewars.com/kata/5808e2006b65bff35500008f/train/python

import string

def position(alphabet):
    alpha = string.ascii_lowercase

    return alpha.index(alphabet) + 1

print(f"Position of alphabet: {position('a')}")