# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

# Exes and Ohs

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and 
# be case insensitive. The string can contain any char.

# Examples input/output:

    # XO("ooxx") => true
    # XO("xooxx") => false
    # XO("ooxXm") => true
    # XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    # XO("zzoo") => false

def xo(s):
#     pass
    if 'x' not in list(s.lower()) and 'o' not in list(s.lower()):
        return True
    
    else:
        if list(s.lower()).count('x') == list(s.lower()).count('o'):
            return True
        
        else:
            return False