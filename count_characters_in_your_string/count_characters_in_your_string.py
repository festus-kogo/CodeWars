# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(s):
    # The function code should be here
    s_unique = set(s)
    result = {}

    if s == "":
        return {}
    
    for x in s_unique:
        result.update({x: s.count(x)})

    return result


print(count('aba'))
print(count(''))
print(count('aa'))
print(count('aabb'))