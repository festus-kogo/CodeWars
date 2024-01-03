# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

def sequence_sum(begin_number, end_number, step):
    #your code here
    sum_total = 0
    
    if begin_number > end_number:
        return 0
    else:
        for i in range(begin_number, end_number + 1, step):
            sum_total += i
        return sum_total
    
print(sequence_sum(2, 2, 2)) # 2
print(sequence_sum(2, 6, 2)) # 12
print(sequence_sum(1, 5, 1)) # 15
print(sequence_sum(1, 5, 3)) # 5
