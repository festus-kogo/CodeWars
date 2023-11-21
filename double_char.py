# https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
# Double Char

text = "String"
# print(list(text))

# arr = []
# for element in list(text):
#     # print(element)
#     arr.append(element * 2)

# print("".join(arr))

def double_char(s):
    # pass
    arr = []
    for element in list(s):
        # print(element)
        arr.append(element * 2)

    return "".join(arr)

print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_ "))