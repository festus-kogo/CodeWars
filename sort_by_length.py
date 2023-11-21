# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python
# Sort array by string length

# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

# For example, if this array were passed as an argument:

    # ["Telescopes", "Glasses", "Eyes", "Monocles"]

# Your function would return the following array:

    # ["Eyes", "Glasses", "Monocles", "Telescopes"]

# All of the strings in the array passed to your function will be different lengths, so you will 
# not have to decide how to order multiple strings of the same length.

s = ["Telescopes", "Glasses", "Eyes", "Monocles"]

# k_v = {}
# for i in s:
#     print(f"Length of {i}: {len(i)}")
#     k_v.update({len(i): i})

# print(k_v)

# keys = []
# for k, v in k_v.items():
#     keys.append(k)

# print(keys)
# keys = sorted(keys)

# print(keys)

# arr = []

# for v in keys:
#     arr.append(k_v[v])

# print(arr)   

def sort_by_length(arr):
    
    def key_value(ar):
        k_v = {}

        for i in ar:
            # print(f"Length of {i}: {len(i)}")
            k_v.update({len(i): i})
        return k_v
    
    def get_keys(d):
        keys = []

        for k, v in d.items():
            keys.append(k)
        return keys
    
    sorted_keys = sorted(get_keys(key_value(arr)))

    arrr = []

    for k in sorted_keys:
        arrr.append(key_value(arr)[k])
    
    return arrr

print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"])) # ['Eyes', 'Glasses', 'Monocles', 'Telescopes']
