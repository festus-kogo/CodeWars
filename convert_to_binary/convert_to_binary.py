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
print(f"{to_binary(128)}") # 10000000

def to_decimal(b):
    dec = [128, 64, 32, 16, 8, 4, 2, 1]
    m_sum = 0

    if len(list(str(b))) != 8:
        l = len(list(str(b)))
        b = "0" * (8 - l) + str(b)
        
    for i, v in enumerate(list(str(b))):
        if int(v) == 1:
            m_sum += dec[i]
    
    return m_sum

print(f"{to_decimal(1)}") # 1
print(f"{to_decimal(10)}") # 2
print(f"{to_decimal(11)}") # 3
print(f"{to_decimal(100)}") # 4
print(f"{to_decimal(10000000)}") # 128




