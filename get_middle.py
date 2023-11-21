# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
# Get the Middle Character

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"

# string = "test"
# print(f"Length {len(string)}") # 4
# print(f"Middle {int(len(string) / 2)}") # 2
# print(string[(2-1):(2+1)]) # es
# print(string[(int(len(string) / 2) - 1):(int(len(string) / 2) + 1)]) # es

# string1 = "testing"
# print(f"Length {len(string1)}") # 7
# print(f"Middle {int(len(string1) / 2)}") # 3
# print(string[int(len(string1) / 2)]) # t

def get_middle(s):
    # pass
    if (len(s) % 2) == 0: # even
        return s[(int(len(s) / 2) - 1):(int(len(s) / 2) + 1)]
    
    return s[int(len(s) / 2)]

print(get_middle("test")) # es
print(get_middle("testing")) # t
print(get_middle("middle")) # dd
print(get_middle("A")) # A
print(get_middle("of")) # of