# Descending Order
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

num = 42145
num_str = str(num)
print(sorted(num_str, reverse=False)) # ['1', '2', '4', '4', '5']
print(sorted(num_str, reverse=True)) # ['5', '4', '4', '2', '1']
print(type(num_str))

def descending_order(num):
    # Bust a move right here
    # pass
    num_str = str(num)
    num_arr = sorted(num_str, reverse=True)
    num_str = "".join(num_arr)
    return num_str

print(descending_order(0)) # 0
print(descending_order(15)) # 51
print(descending_order(123456789))