# https://www.codewars.com/kata/56efc695740d30f963000557/train/python
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe

# string = "hello world"
# print(list(string))

def to_alternating_case(string):
    arr = []

    for ch in list(string):
        if ch.isupper():
            arr.append(ch.lower())
        else:
            arr.append(ch.upper())

    return "".join(arr)


print(to_alternating_case("hello world")) # HELLO WORLD
print(to_alternating_case("HELLO WORLD")) # hello world
print(to_alternating_case("hello WORLD")) # HELLO world
print(to_alternating_case("HeLLo WoRLD")) # hEllO wOrld
print(to_alternating_case("12345"), "12345") # 12345
print(to_alternating_case("1a2b3c4d5e")) # 1A2B3C4D5E