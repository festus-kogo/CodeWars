def invert(lst):
    result = []

    if lst == []:
        return lst
    
    for i in lst:
        if i < 0 : # Negative number
            result.append(abs(i))
        else:
            result.append(-abs(i))
    
    return result

print(invert([1,2,3,4,5])) # [-1, -2, -3, -4, -5]
print(invert([1,-2,3,-4,5])) # [-1, 2, -3, 4, -5]
print(invert([]))
    
    
