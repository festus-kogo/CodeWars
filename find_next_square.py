# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
# Find the next perfect square!
import math 
print(math.isqrt(100)) # 10
print(math.isqrt(10)) # 3
# print(math.sqrt(100)) # 10.0
# print(math.sqrt(10)) # 3.1622776601683795
print(type(int(math.sqrt(9))))

def isPerfect(n):
    sqrt = math.isqrt(n)

    if sqrt * sqrt == n:
        return True
    
    return False

print(isPerfect(100)) # true
print(isPerfect(10)) # false
print(isPerfect(1000)) # false

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    def isPerfect(n):
        sqrt = math.isqrt(n)

        if sqrt * sqrt == n:
            return True
        
        return False
    
    if isPerfect(sq) == True:
        return (math.isqrt(sq) + 1) ** 2

    return -1

print(find_next_square(100)) # 121
print(find_next_square(121)) # 144
print(find_next_square(144)) # 169
print(find_next_square(625)) # 676
print(find_next_square(114)) # 169
