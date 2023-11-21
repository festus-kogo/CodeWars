# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

num = 2
num = 8
total = 0
for i in range(1, num + 1):
    # print(i)
    total += i

print(f"total: {total}")

def summation(num):
    # Code here
    total = 0
    for i in range(1, num + 1):
        # print(i)
        total += i

    return total

print(f"summation: {summation(2)}")
print(f"summation: {summation(8)}")