# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
# The Supermarket Queue

def queue_time(customers, n):
    # pass # TODO
    if customers == []:
        return 0
    
    elif len(customers) == 1:
        return customers[0]
    
    else:
        if n == 1:
            total_sum = 0
            for element in customers:
                total_sum += element
            return total_sum
        
        elif max(customers) == customers[0]:
            return customers[0]




print(queue_time([5,3,4], 1)) # 12
print(queue_time([], 1)) # 0
print(queue_time([2], 5)) # 2
print(queue_time([10,2,3,3], 2)) # 10
print(queue_time([1000,2,3,3], 2)) # 1000
# print(max([10,2,3,3,100,100]))
