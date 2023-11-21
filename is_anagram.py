# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
# Anagram Detection
test = "dumble"
original = "bumble"
test = sorted(test)
original = sorted(original)
# print(test)
# print(original)

for j in test:
    # print(j)
    if j in original:
        print(True)
    else:
        print(False)

# write the function is_anagram
def is_anagram(test, original):
    test = sorted(test.lower())
    original = sorted(original.lower())
    output = False

    print(test)
    print(original)

    if len(test) == len(original):
        for j in test:
            if j in original:               
                output = True
            else:
                output = False

    return output

print(is_anagram("foefet", "toffee")) # True
print(is_anagram("Buckethead", "DeathCubeK")) # True
print(is_anagram("Twoo", "WooT")) # True
print(is_anagram("dumble", "bumble")) # False
# print(is_anagram("ound", "round")) # False
# print(is_anagram("apple", "pale")) # False

# print(len('xlCzlBQIbYGTWcw'))
# print(len('lwWxozxEBQTlFCV'))
# print(sorted('xlCzlBQIbYGTWcw'.lower()))
# print(sorted('lwWxozxEBQTlFCV'.lower()))