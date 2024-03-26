# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python

def sum_mul(n, m):
    sum_total = 0

    if n < 1 or m < 1:
        return "INVALID"
    
    for i in range(n, m, n):
        # print(f"i => {i}")
        sum_total += i

    return sum_total


print(f"{sum_mul(2, 9)}")
print(f"{sum_mul(3, 13)}")