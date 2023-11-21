# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
# Are they the "same"?

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a = sorted(a) 
b = sorted(b)

# print(len(a))
# print(len(b))

# for i in range(len(a)):
#     if (a[i] ** 2) == b[i]:
#         print("True")

#     else:
#         print("False")

def comp(array1, array2):
    # your code
    array1 = sorted(array1)
    array2 = sorted(array2)

    for i in range(len(array1)):
        if (array1[i] ** 2) in array2:
            return False        
        else:
            return True
    # pass

print(comp(a, b)) # True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) # True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) # False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(sorted(a1))
print(sorted(a2))

print(comp(a1, a2)) # False