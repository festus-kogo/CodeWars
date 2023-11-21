# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python

# Invert values
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

#     invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
#     invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
#     invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    # pass
    inverted = []
    # print(inverted)

    if len(lst) == 1 and lst[0] == 0:
        inverted = []
    
    elif len(lst) == 0:
        inverted.append(abs(0))

    else:        
        for element in lst:
            if element > 0: # Positive. Convert to negative
                # inverted.append(int('-' + str(element)))
                inverted.append(-abs(element))
            elif element < 0: # Negative. Convert to positive
                inverted.append(abs(element))
    
    return inverted

# print(invert([1,2,3,4,5])) # [-1, -2, -3, -4, -5]

# print(invert([1,-2,3,-4,5])) # [-1, 2, -3, 4, -5]
# print(invert([])) # []
print(invert([0])) # []
print(invert([])) # [0]