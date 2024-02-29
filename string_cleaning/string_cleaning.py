# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def single_string(s):
    return "".join([l for l in s if l not in nums])

# print(f"{single_string('looks5')}") # looks
# print(f"{single_string('123456789')}") # 

def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    
    # Split string
    if s == "":
        return ""

    return " ".join([single_string(s1) for s1 in s.split(" ")])

print(f"Output => {string_clean('A1 A1! AAA   3J4K5L@!!!')}") # A A! AAA   JKL@!!!
