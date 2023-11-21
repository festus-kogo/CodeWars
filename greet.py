# https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python

# Grasshopper - Personalized Message

# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

#     case	               return
#     name equals owner	   'Hello boss'
#     otherwise	           'Hello guest'

def greet(name, owner):
    # Add code here
    if name is owner:
        return 'Hello boss'
    
    return 'Hello guest'