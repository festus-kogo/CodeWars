# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
# Count the divisors of a number
n = 4 # [1, 2, 4]
n = 5 # [1, 5]
n = 12 # [1, 5]
n = 30 # [1, 2, 3, 5, 6, 10, 15, 30]
arr = [] # [1, 2, 3, 4, 6, 12]

for i in range(n):
    # print(i)
    if n % (i + 1) == 0:
        arr.append(i + 1)

print(len(arr))

def divisors(n):
    # pass
    arr = []

    for i in range(n):
        # print(i)
        if n % (i + 1) == 0:
            arr.append(i + 1)

    return len(arr)

print(divisors(1)) # 1
print(divisors(4)) # 3
print(divisors(5)) # 2
print(divisors(12)) # 6
print(divisors(30)) # 8
print(divisors(4096)) # 13