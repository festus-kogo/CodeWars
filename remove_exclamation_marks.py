# https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    #your code here
    arr = []
    
    for i in list(s):
        if i != "!":
            arr.append(i)
            
    return "".join(arr)
    
        