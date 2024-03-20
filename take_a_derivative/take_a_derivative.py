# https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python

def derive(coefficient, exponent): 
    # your code here
    return f"{coefficient * exponent}x^{exponent - 1}"

print(f"{derive(7,8)}") # 56x^7
print(f"{derive(5,9)}") # 45x^8
