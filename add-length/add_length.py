# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

def add_length(str_):
    #your code here
    arr = []

    for i in str_.split():
        _str = i + " " + str(len(i))
        arr.append(_str)
    
    return arr

print(add_length('apple ban'))
print(add_length('you will win'))
print(add_length('you'))
print(add_length('y'))