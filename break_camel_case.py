# codewars.com/kata/5208f99aee097e6552000148/train/python
# Break camelCase

s = "helloWorld"
s = "breakCamelCase"
# arr = []

# for character in s:
#     if character.isupper() == True:
#         new_character = "#"
#         # print(new_character)
#         arr.append(new_character)
#     # print(character)
#     arr.append(character)
# print(arr)

# s1 = "".join(arr)
# print(s1)

# s2 = s1.split("#")
# print(s2)

# s3 = " ".join(s2)
# print(s3)

def solution(s):
    arr = []

    for character in s:
        if character.isupper() == True:
            arr.append("#")
        arr.append(character)
    # print(arr) # ['b', 'r', 'e', 'a', 'k', '#', 'C', 'a', 'm', 'e', 'l', '#', 'C', 'a', 's', 'e']

    s1 = "".join(arr)
    # print(s1) # break#Camel#Case

    s2 = s1.split("#")
    # print(s2) # ['break', 'Camel', 'Case']

    s3 = " ".join(s2)
    # print(s3) # break Camel Case

    return s3

print(solution(s))

def splitstring(mystring:str):
    mystring1 = mystring

    if mystring1 == "":
        return ""
    else:
        for x in mystring1:
            # print(x)
            if x.isupper() == True:
                # mystring1 = mystring1.replace(x," " +x)
                if x.isspace() == True:
                    continue
                else:
                    mystring1 = mystring1.replace(x," " +x)
        
        return mystring1

# print(splitstring("")) # ""
# print(splitstring("camelCasing")) # camel Casing
# splitstring("breakCamelCase") # 
# print(splitstring("breakCamelCase"))
# print(splitstring("camelCasingCamelCasingCamelCasing")) # break Camel Case