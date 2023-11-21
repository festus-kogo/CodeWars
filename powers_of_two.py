# https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python
# Powers of 2

# print(2 ** 0)
# arr = []
# for i in range(1):
#     print(f"i: {i}")
#     arr.append(2**i)

# print(arr)

def powers_of_two(n):
    arr = []
    for i in range(n + 1):
        # print(f"i: {i}")
        # pwr_of_two = 2 * i
        # print(f"pwr_of_two: {pwr_of_two}")
        arr.append(2 ** i)

    return arr

print(powers_of_two(0))
print(powers_of_two(1))
print(powers_of_two(4))