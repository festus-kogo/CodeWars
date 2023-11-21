# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
# Sum without highest and lowest number

def sum_array(arr):
    #your code here
    if arr == None or arr == [] or arr == "" or len(arr) == 1:
        return 0
    
    sum = 0
    highest = max(arr)
    lowest = min(arr)
    
    for i in arr:
        sum += i
        
    
    return sum - (highest + lowest)