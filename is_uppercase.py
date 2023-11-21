# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
# Is the string uppercase?


def is_uppercase(inp):
    arr = []

    for element in inp:
        if element.islower() == True:
            arr.append(1)
        elif element.isupper() == True:
            arr.append(2)
    
    # Now check what is in arr
    if 1 in arr:
        return False
    
    return True

    
print(is_uppercase("c")) # False
print(is_uppercase("C")) # True
print(is_uppercase("hello I AM DONALD")) # False
print(is_uppercase("HELLO I AM DONALD")) # True
print(is_uppercase("$%&")) # True
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ")) # False