# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import string

def get_number_part(s): # returns a tupple of string type
    s1 = s[::-1] # Reverse
    temp = s1
    alphabet = string.ascii_letters
    numbers = "0123456789"
        
    for i, l in enumerate(s1):
        if l in alphabet or l not in numbers:
            return (temp[:i])[::-1],  (temp[i:])[::-1] # Reverse number_part, str_part
        
    return (str(s), '')


def increment_string(strng):

    print(f"strng is ==> {strng} of type {type(strng)}")

    if strng == "": # if parameter is empty then return '1'
        return str(1)

    else: # Go ahead and unpack the function
        result = get_number_part(strng)
        number_part, str_part = result

        if number_part == "":
            return str_part + str(1)
        
        elif str_part == "":
            output = int(number_part) + 1
            number_part_len = len(number_part)
            output_len = len(str(output))            

            if output_len < number_part_len:
                leading_zeros = "0" * (number_part_len - output_len)
                return str(leading_zeros) + str(output)

            return str(output)
        
        else:
            output = int(number_part) + 1
            output_len = len(str(output))

            if output_len < number_part_len:
                leading_zeros = "0" * (number_part_len - output_len)
                return str_part + str(leading_zeros) + str(output)

        return str_part + str(output)

