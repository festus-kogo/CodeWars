# https://www.codewars.com/kata/524f5125ad9c12894e00003f/train/python

def remainder(a,b):
    #your code here
    data = [a, b]

    if min(data) == 0:
        return None
    
    return max(data) % min(data)

print(f"{remainder(17,5)}") # 2
print(f"{remainder(13, 72)}") # 
print(f"{remainder(1, 0)}") # None
print(f"{remainder(0, 0)}") # None
print(f"{remainder(0, 1)}") # None
print(f"{remainder(-1, 0)}") # 0
print(f"{remainder(0, -1)}") # 0
print(f"{remainder(-13, -13)}") # 0
print(f"{remainder(-60, 340)}") # -20
print(f"{remainder(60, -40)}") # -20
