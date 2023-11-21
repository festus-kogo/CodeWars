# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# Beginner Series #3 Sum of Numbers

# a ,b = (1, 0)
# a, b = sorted((1, 0))
# print(a, b)
# for i in range(b + 1):
#     print(i)

# if a == b:
#     return a

def get_sum(a, b):
    # good luck!
    a, b = sorted((a, b))
    my_sum = 0

    for i in range(a, (b + 1)):
        my_sum += i

    
    return my_sum

print(get_sum(1, 0)) # 1
print(get_sum(1, 2)) # 3
print(get_sum(0, 1)) # 1
print(get_sum(1, 1)) # 1
print(get_sum(-1, 0)) # -1
print(get_sum(-1, 2)) # 2

