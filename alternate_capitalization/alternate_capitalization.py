# https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python

def capitalize(s):
    arr  = []
    arr1 = []
    s = list(s)

    for i, l in enumerate(s):
        if i % 2 != 0: # Odd index
            arr.append(l)
            arr1.append(l.upper())
        else:
            arr.append(l.upper())
            arr1.append(l)
    return ["".join(arr), "".join(arr1)]
        

print(capitalize("abc"))
print(capitalize("abcdef"))
print(capitalize("codewars"))
print(capitalize("codewarriors"))