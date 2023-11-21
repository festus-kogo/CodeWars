# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

# Counting Duplicates

# Check break the string into a list
text = "abcde"
text = "acCCdDDDDDe"
text_list = list(text.lower())
print(f"text_list: {text_list}") # ['a', 'b', 'c', 'd', 'e']

char_list = []

for ch in text_list:
     if ch not in char_list:
          char_list.append(ch)

print(char_list)

print(f"Count: {text_list.count('a')}") # 3
print(f"Count: {text_list.count('b')}") # 3
print(f"Count: {text_list.count('c')}") # 3
print(f"Count: {text_list.count('d')}") # 6

duplicate_counter = []
for ch in char_list:
     if text_list.count(ch) > 1:
          duplicate_counter.append(ch)

print(f"duplicate_counter {duplicate_counter}")
print(f"output {len(duplicate_counter)}")
##########################################################################################
def duplicate_count(text):
    # Your code goes here
    text_list = list(text.lower())

    char_list = []

    for ch in text_list:
        if ch not in char_list:
            char_list.append(ch)

    duplicate_counter = []
    for ch in char_list:
        if text_list.count(ch) > 1:
            duplicate_counter.append(ch)

    if len(duplicate_counter) == 0:
        return 0
    
    return len(duplicate_counter)

##########################################################################################
# test
print(duplicate_count("abcde")) # 0
print(duplicate_count("aabbcde")) # 2
print(duplicate_count("aabBcde")) # 2
print(duplicate_count("indivisibility")) # 1
print(duplicate_count("Indivisibilities")) # 2
print(duplicate_count("aA11")) # 2
print(duplicate_count("ABBA")) # 2