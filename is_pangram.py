# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# Detect Pangram

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence 
# "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string

print(string.ascii_lowercase)

def is_pangram(s):
    for letter in string.ascii_lowercase:
        # print(letter)
        # if letter in list("The quick brown fox jumps over the lazy dog"):
        if letter not in list(set(list(s.lower()))):
            # print(letter)
            return False
        
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))

# print(list("The quick brown fox jumps over the lay dog"))
# print(list(set(list("The quick brown fox jumps over the lay dog"))))