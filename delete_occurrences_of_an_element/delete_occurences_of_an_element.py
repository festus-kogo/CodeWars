# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order, max_e):
    # code here
    arr = []

    for element in order:
        if  arr.count(element) < max_e:
            arr.append(element)

    return arr

print(delete_nth([20,37,20,21], 1)) # [20, 37, 21]
# print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) # [1, 1, 3, 3, 7, 2, 2, 2]
print(delete_nth([1,2,3,1,1,2,1,2,3,3,2,4,5,3,1], 3))
# [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1]
# [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 4, 5]