# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

# Reverse words

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

#     Examples
#     "This is an example!" ==> "sihT si na !elpmaxe"
#     "double  spaces"      ==> "elbuod  secaps"

string = "double  spaces"
"double  spaces"
"double  spaces"
"double  spaces"

splitted = []
for  word in string.split(" "):
    # print(word)
    # if word == "":
    #     splitted.append("this_is_a_space")
    
    splitted.append(word)

# print(splitted)
# print(type(splitted))
# print(f"splitted len: {len(splitted)}")

string1 = " ".join(splitted)
# print(string1)

# print("Hello".split()) # ['Hello']
# print(list("Hello")) # ['H', 'e', 'l', 'l', 'o']

"e,l,b,u,o,d  s,e,c,a,p,s"

"elbuod  secaps"
"double  spaces"

###################################################################################
def reverse_words(text): # e.g "Hello World"
  #go for it
    final_arr = []
    splitted = text.split(" ")

    def reverse_func(s): # Takes in a word or empty string e.g "Hello", ""
        # string_lst = s.split()
        string_lst = list(s)
        # print(string_lst)
        count = len(string_lst)
        i = 1
        lst = []

        while i <= count:
            item_pos = -abs(i)
            lst.append(string_lst[item_pos])
            i += 1
        # print(f"lst: {lst}")
        return "".join(lst)
    
    for word in splitted:
        # print(f"word: {word}")
        final_arr.append(reverse_func(word))
        # final_arr.append(word)

    output = " ".join(final_arr)
    return output

print(reverse_words("double  spaces")) # elbuod  secaps
print(reverse_words("This is an example!")) # !elpmaxe na si sihT

###################################################################################
"sihT si na !elpmaxe"
"sihT si na !elpmaxe"

"elbuod  secaps"
"elbuod  secaps"

# print(reverse_words("Hello")) # olleH
# print(reverse_words("double  spaces")) # elbuod secaps
print(reverse_words("double  spaces")) # elbuod  secaps
print(reverse_words("hello  spaces")) # olleh  secaps
print(reverse_words("hello spaces")) # olleh secaps
print(reverse_words("hellospaces")) # secapsolleh
# print(reverse_words("What!")) # !tahW
print(reverse_words("This is an example!")) # !elpmaxe na si sihT
# print(reverse_words("olleH")) # Hello
# print(reverse_words("elbuod decaps sdrow")) # double spaced words
# print(reverse_words("elbuod")) # double
# print(reverse_words("decaps")) # spaced
# print(reverse_words("sdrow")) #  words

'elbuod  decaps  sdrow'
string = 'double  spaced  words'
# print(string.split())
# print(list(string))
# print(list("Hello"))

# print(len('double  spaced  words'))
# string = 'one  two'
# string = "double  spaced  words"
# # double  spaced  words
# # double  spaced  words
# arr = list(string)
# arr = string.split(" ")
# print(arr)

# for i in arr:
#     space = " "
#     if i == " ":
#         print(space)

#     print(i, end=" ")
