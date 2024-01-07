# https://www.codewars.com/kata/59ca8e8e1a68b7de740001f4/train/python

def solve(a,b):
    arr = []

    for i in b:
        arr.append(a.count(i))
    
    return arr

# print(solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap'])) # [2, 1, 0]
# print(solve(['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz'])) # [2, 1, 2]
print(solve(['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox']))