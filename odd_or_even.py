# https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

#     Examples:
#     Input: [0]
#     Output: "even"

#     Input: [0, 1, 4]
#     Output: "odd"

#     Input: [0, -1, -5]
#     Output: "even"

def odd_or_even(arr):
    # pass
    sum_arr = 0
    output = ""

    if len(arr) == 0:
        output = "even"
    else:
        for element in arr:
            sum_arr += element
        
        if sum_arr % 2 == 0:
            # Even
            output = "even"
        else:
            output = "odd"
        
    return output

print(odd_or_even([0])) # even
print(odd_or_even([0, -1, -5])) # even
print(odd_or_even([0, 1, 4])) # odd