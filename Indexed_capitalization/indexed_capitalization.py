# https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python

def capitalize(s, ind):
    s = list(s)
    arr = []

    for i, l in enumerate(s):
        if i in ind:
            arr.append(l.upper())
        else:
            arr.append(l)
    
    return "".join(arr)

print(capitalize("abcdef",[1,2,5])) # aBCdeF
# aBCdeF
# aBCdeF

print(capitalize("abracadabra",[2,6,9,10])) # abRacaDabRA
# abRacaDabRA
# abRacaDabRA

print(capitalize("codewarriors",[5])) # codewArriors
# codewArriors
# codewArriors

print(capitalize("abcdef",[1,2,5,100])) # aBCdeF
# aBCdeF
# aBCdeF

print(capitalize("codewars",[1,3,5,50])) # cOdEwArs
# cOdEwArs
# cOdEwArs