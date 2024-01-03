# https://tryhackme.com/room/introwebapplicationsecurity

# Relying on a weak cryptographic algorithm. One old cryptographic algorithm is to shift each letter by one. 
# For instance, “TRY HACK ME” becomes “USZ IBDL NF.” This cryptographic algorithm is trivial to break.


import string

def encrypt_text(s):
    letters = string.ascii_uppercase
    s = list(s)
    arr = []

    for c in s:
        if c in letters:
            if s.index(c) == 25:
                arr.append(s[0])
            else:
                arr.append(letters[letters.index(c) + 1])
        else:
            arr.append(" ")
    
    return ''.join(arr)


print(f"{encrypt_text('TRY HACK ME')}")

