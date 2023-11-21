# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
# Unique In Order

text = 'AAAABBBCCDAABBB'
text = list(text)
# print(set(list(text)))
print(text)
print(text[0 + 1])

for i, element in enumerate(text):
    print(str(i) + " => " + element)
    next_pos = i + 1
    next_element = text[int(next_pos)]
    print(f"next_pos: {next_pos}")
    print(f"next_element: {next_element}")
    if element == next_element:
        text.pop(next_pos)

def unique_in_order(sequence):
    return