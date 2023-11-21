# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

# Example
    # wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
string = "hello"
string = "two words"
splitted = list(string)
# print(splitted[0]) # h
# splitted[0] = splitted[0].upper()
# print(splitted)

arr = []
spacer = ""
# print(spacer)
for ch in range(len(splitted)):
    splitted1 = list(string)
    if splitted1[ch] == spacer:
        # splitted1[ch + 1] = splitted1[ch + 1].upper()
        continue
    # print(ch)
    # print(splitted1[ch])
    else:
        splitted1[ch] = splitted1[ch].upper()
    
    arr.append("".join(splitted1))

# print(arr) # ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
# print(arr) # []

def wave(people):
    # Code here 
    splitted = list(people)
    # print(splitted[0]) # h
    # splitted[0] = splitted[0].upper()
    # print(splitted)
    spacer = " "
    arr = []

    for i in range(len(splitted)):
        splitted1 = list(people)
        if splitted1[i] == spacer: # if empty e.g "" then skip and move to the next
            continue
        # print(ch)
        # print(splitted1[ch])
        else:
            splitted1[i] = splitted1[i].upper()
        
        arr.append("".join(splitted1))
    
    return arr

# print(wave("hello")) # ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
# print(wave("gap")) # ['Gap', 'gAp', 'gaP']
# print(wave("codewars")) # ['Codewars', 'cOdewars', 'coDewars', 'codEwars', 'codeWars', 'codewArs', 'codewaRs', 'codewarS']
# print(wave("gap")) # ['Gap', 'gAp', 'gaP']
# print(wave("")) # []
# print(wave("two words")) # ['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']
print(wave("this is a few words")) #