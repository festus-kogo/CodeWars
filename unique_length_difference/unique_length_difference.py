# https://www.codewars.com/kata/5663f5305102699bad000056/train/python

def mxdiflg(a1, a2):
    # your code
    temp_mx = 0

    if a1 == [] or a2 == []:
        return -1

    for x in a1:
        for y in a2:
            # print(f"abs({len(x)} - {len(y)}) is {abs(len(x) - len(y))}")
            if abs(len(x) - len(y)) > temp_mx:
                temp_mx = abs(len(x) - len(y))
    return temp_mx