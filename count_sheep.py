# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python
# If you can't sleep, just count sheep!!

def count_sheep(n):
    # your code
    arr = []

    if n == 0:
        return ""
    
    for i in range(n):
        arr.append(f"{i + 1} sheep...")
    
    return "".join(arr)



print(count_sheep(0))
print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))