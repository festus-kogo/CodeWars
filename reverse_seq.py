# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

# Build a function that returns an array of integers from n to 1 where n>0.

#     Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    # pass
    arr = []
    count = n

    while count > 0:
        arr.append(count)
        count -= 1
        
    return arr

print(reverse_seq(5))