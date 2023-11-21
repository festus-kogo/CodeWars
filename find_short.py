# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

# Shortest Word

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# s = "bitcoin take over the world maybe who knows perhaps"
# splitted = s.split(" ")

# print(splitted)

# temp_shortest = len(splitted[0])

# for word in splitted:
#     # if len(word) < temp_shortest:
#     if temp_shortest > len(word):
#         temp_shortest = len(word)

# print(temp_shortest) # 3

def find_short(s):
    # your code here
    splitted = s.split(" ")
    temp_shortest = len(splitted[0])

    for word in splitted:
        if temp_shortest > len(word):
            temp_shortest = len(word)

    return temp_shortest

print(find_short("bitcoin take over the world maybe who knows perhaps")) # 3
print(find_short("turns out random test cases are easier than writing out basic ones")) # 3
print(find_short("lets talk about javascript the best language")) # 3
print(find_short("i want to travel the world writing code one day")) # 1
print(find_short("Lets all go on holiday somewhere very cold")) # 2
print(find_short("Let's travel abroad shall we")) # 2