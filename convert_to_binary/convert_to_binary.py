# https://www.codewars.com/kata/59fca81a5712f9fa4700159a/train/python


def to_binary(n):
    #your code here
    div = n
    mods = []

    while div != 0:      
        div, mod = divmod(div, 2)
        mods.append(str(mod))
    
    return int("".join(mods[::-1]))
    
print(f"{to_binary(1)}") # 1
print(f"{to_binary(2)}") # 10
print(f"{to_binary(3)}") # 11
print(f"{to_binary(4)}") # 100


