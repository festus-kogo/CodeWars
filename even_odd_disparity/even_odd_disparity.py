# https://www.codewars.com/kata/59c62f1bdcc40560a2000060/train/python

def solve(a):
    even = []
    odd = []
    
    for i in a:
        if type(i) is not str:
            if i % 2 == 0: # Even number
                even.append(i)
            elif i % 2 != 0: # Odd  number
                odd.append(i)
    
    return len(even) - len(odd)

print(solve([0,1,2,3])) # 0
print(solve([0,1,2,3,'a','b']))
print(solve([0, 15,'z',16,'m', 13, 14,'c', 9, 10, 13,'u', 4, 3]))
print(solve([13, 6, 8, 15, 4, 8, 13]))
print(solve([1,'a', 17, 8,'e', 3,'i', 12, 1]))