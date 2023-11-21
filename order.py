# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

# Your order, please

# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position 
# the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
    # "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
    # "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    # ""  -->  ""

# sentence = "is2 Thi1s T4est 3a"
# splitted = sentence.split(" ")
# splitted2 = sentence.split(" ")
# # print(splitted2)
# for word in splitted:
#     for ch in word:
#         if ch.isnumeric():
#             splitted2[int(ch) - 1] = word

# print(splitted2)

def order(sentence):
  # code here
    splitted = sentence.split(" ")
    splitted2 = sentence.split(" ")

    for word in splitted:
        for ch in word:
            if ch.isnumeric():
                splitted2[int(ch) - 1] = word
    
    return " ".join(splitted2)

print(order("is2 Thi1s T4est 3a")) # "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2")) # "Fo1r the2 g3ood 4of th5e pe6ople"
print(order("")) # ""


