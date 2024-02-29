# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    index = 0
    for i, j in enumerate(arr):
        # print(f"At index {i} sum left => {sum(arr[:i])} sum right => {sum(arr[(i + 1):])}")
        if sum(arr[:i]) == sum(arr[(i + 1):]):
            index = i
            break
        else:
            index = -1

    return index

print(f"{find_even_index([1,2,3,4,3,2,1])}") # 3
print(f"{find_even_index([1,100,50,-51,1,1])}") # 1
print(f"{find_even_index([1,2,3,4,5,6])}") # -1
print(f"{find_even_index([20,10,30,10,10,15,35])}") # 3
print(f"{find_even_index([20,10,-80,10,10,15,35])}") # 0
print(f"{find_even_index([10,-80,10,10,15,35,20])}") # 6

