# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
# Highest Scoring Word

import string
alphabets = string.ascii_lowercase
# print(list(alphabets))
# print(list(alphabets)[0])

word = "abad"
word = "aa"

def word_score(w):
    score = 0

    for letter in list(w):
        if letter in alphabets:
            # print(f"Found {letter} at position {alphabets.index(letter) + 1}")
            score += (alphabets.index(letter) + 1)

    return score

text = "aaa b"

score_dict = {}
for word in text.split():
    # print(word)
    score_dict.update({word: word_score(word)})

# print(score_dict) # {'man': 28, 'i': 9, 'need': 28, 'a': 1, 'taxi': 54, 'up': 37, 'to': 35, 'ubud': 48}

scores = set()
for key, value in score_dict.items():
    scores.add(value)

# print(scores) # {2, 3}
# print(max(scores)) # 3

for key, value in score_dict.items():
    if value == max(scores):
        # print(key)
        # break
        pass
# print(word_score("abad")) # 8
# print(word_score("aa")) # 2
def high(x):
    # Code here

    alphabets = string.ascii_lowercase

    def word_score(w):
        score = 0

        for letter in list(w):
            if letter in alphabets:
                # print(f"Found {letter} at position {alphabets.index(letter) + 1}")
                score += (alphabets.index(letter) + 1)
        return score

    score_dict = {} # word: score dictionary
    for word in x.split():
        # print(word)
        score_dict.update({word: word_score(word)})

    # print(score_dict) # {'man': 28, 'i': 9, 'need': 28, 'a': 1, 'taxi': 54, 'up': 37, 'to': 35, 'ubud': 48}

    scores = set() # set() of scores
    for key, value in score_dict.items():
        scores.add(value)

    for key, value in score_dict.items():
        # print(k)
        if value == max(scores):
            return key
        

print(high('man i need a taxi up to ubud')) # taxi
print(high('what time are we climbing up the volcano')) # volcano
print(high('take me to semynak')) # semynak
print(high('aa b')) # aa
print(high('b aa')) # b
print(high('bb d')) # bb