# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

# Vowel Count

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

string = "Hello world" # ['Hello', 'world']

print(string.split(" "))

print("".join(string.split(" ")))

def get_count(sentence):    
    count = 0
    splitted = sentence.split(" ") # ['Hello', 'world']

    for vowel in "".join(splitted): # 'Helloworld'
        if vowel in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    
    return count

    


get_count("Hello world")
print(get_count("Hello world"))