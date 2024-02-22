# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

def n_by_n_array(arr, n):
    lst1 = []
    for i in arr:
        lst1.append(i * n)
    
    return lst1

def multiplication_table(size):
    lst = [i + 1 for i in range(size)]
    lst1 = [n_by_n_array(lst, i) for i in range(1, size + 1)]
    return lst1

print(f"{multiplication_table(1)}") # [[1]]
print(f"{multiplication_table(2)}") # [[1, 2], [2, 4]]
print(f"{multiplication_table(3)}") # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
print(f"{multiplication_table(4)}") # [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
print(f"{multiplication_table(5)}") # [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]