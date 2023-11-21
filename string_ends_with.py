# Source https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

# String ends with?

# Complete the solution so that it returns true if the first argument(string) passed in ends with 
# the 2nd argument (also a string).

# Examples:
    # solution('abc', 'bc') # returns true
    # solution('abc', 'd') # returns false
text = 'abc'
text2 = 'bc'
print(len(text2))
print(text[-2:]) 

def solution(text, ending):
    # your code here...
    # pass
    if text[-len(ending):] == ending:
        return True
    
    return False

