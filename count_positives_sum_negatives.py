# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python


# Count of positives / sum of negatives

# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

#     Example
#     For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


def count_positives_sum_negatives(arr):
    final_arr = []
    positive_num_count = 0
    negative_num_sum = 0

    if len(arr) == 0:
        final_arr = []
    else:
        for element in arr:
            if element > 0: # Positive number
                positive_num_count += 1
            else:
                negative_num_sum += abs(element)
        
        final_arr.append(positive_num_count)
        final_arr.append(-abs(negative_num_sum))

    return final_arr

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([]))