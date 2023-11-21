# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
# Find the capitals

# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

# Example (Input --> Output)

    # "CodEWaRs" --> [0,3,4,6]

def capitals(word):
    #your code here
    arr = []
    for i, ch in enumerate(word):
        # print(ch)
        if word[i].isupper() == True:
            # print("Upercase")
            arr.append(i)
    
    return arr

print(capitals("fdWFfRmSIxPDunMwBWQIeeYqE"))
# [2, 3, 5, 7, 8, 10, 11, 14, 16, 2, 18, 8, 22, 24]
# [2, 5, 7, 8, 13, 14, 15, 18, 19, 21, 22]