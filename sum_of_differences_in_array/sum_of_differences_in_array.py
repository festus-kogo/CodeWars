# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/python

def sum_of_differences(arr):

    m_sum = 0

    if arr == "" or len(arr) == 1: 
        return 0
    
    for i in range(len(arr) - 1):
        # print(f"{sorted(arr)[::-1][i]} - {sorted(arr)[::-1][i + 1]}")

        m_sum += (sorted(arr)[::-1][i] - sorted(arr)[::-1][i + 1])
    
    return m_sum

print(f"{sum_of_differences([1, 2, 10])}")
print(f"{sum_of_differences([-3, -2, -1])}")
print(f"{sum_of_differences([1, 1, 1, 1, 1])}")
print(f"{sum_of_differences([-17, 17])}")
print(f"{sum_of_differences([])}")
print(f"{sum_of_differences([0])}")
print(f"{sum_of_differences([-1])}")
print(f"{sum_of_differences([1])}")