def binary_array_to_number(arr):
  # your code
    arr_str = ''.join(str(element) for element in arr)
    return int(arr_str, 2)

print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([0, 1, 0, 1]))
print(binary_array_to_number([1, 0, 0, 1]))