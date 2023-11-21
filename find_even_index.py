# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

# Equal Sides Of An Array

def digitize(n):
    arr = []
    arr_lst = list(str(n))
    count = 1
    i = 0

    if n == 0:
        return [0]
    else:
        while count <= len(arr_lst):
            item_pos = -abs(count)
            arr.append(int(arr_lst[item_pos]))
            count += 1
            
        return arr

print(digitize(35231)) # [1,3,2,5,3]
print(digitize(0)) # [0]
print(digitize(23582357)) # [7,5,3,2,8,5,3,2]
print(digitize(984764738))
print(digitize(45762893920))
print(digitize(548702838394))
