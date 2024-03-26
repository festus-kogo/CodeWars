# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    # your code
    sum_total = 0

    for i, x in enumerate(str(n)):
        sum_total += int(x) ** (p + i)

    if (sum_total / n).is_integer(): # returns True or False
        return int(sum_total / n)
    
    return -1



    # return -1
        
print(f"{dig_pow(89, 1)}")
print(f"{dig_pow(92, 1)}")
print(f"{dig_pow(46288, 3)}")
print(f"{dig_pow(41, 5)}")
print(f"{dig_pow(114, 3)}")
print(f"{dig_pow(8, 3)}")