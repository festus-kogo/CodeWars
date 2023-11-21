# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

# Mumbling

# This time no story, no theory. The examples below show you how to write function accum:

#     Examples:
#     accum("abcd") -> "A-Bb-Ccc-Dddd"
#     accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#     accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

text = "RqaEzty"
# text = "a"
text_list = list(text)
arr = []

for i in range(len(text_list)):
    # print(i)
    if i == 0:
        if text_list[i].islower():
            arr.append(text_list[i].upper())
        elif text_list[i].isupper():
            arr.append(text_list[i].lower())

    else:# When i is not 0
        if text_list[i].islower():
            arr.append(text_list[i].upper() + "" + (text_list[i].lower() * i))
        elif text_list[i].isupper():     
            arr.append(text_list[i].lower() + "" + (text_list[i].upper() * i))
    
    
# print(arr)
# print("-".join(arr))

#####################################################################################
def accum(s):
    # your code
    text_list = list(s)
    arr = []

    for i in range(len(text_list)):
        if i == 0:

            arr.append(text_list[i].upper())
        else:
            arr.append(text_list[i].upper() + "" + (text_list[i] * i).lower())

    return "-".join(arr)
#####################################################################################

print(accum("ZpglnRxqenU"))
# Output
"Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
"Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"

# print(accum("R")) # R

# print(accum("abcd"))
# Output
"A-Bb-Ccc-Dddd"
"A-Bb-Ccc-Dddd"

# print(accum("RqaEzty"))
# Output
"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

# print(accum("cwAt"))
# Output
"C-Ww-Aaa-Tttt"
"C-Ww-Aaa-Tttt"