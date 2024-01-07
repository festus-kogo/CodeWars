# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def get_product(num):
    num_arr = list(str(num))
    product = 1

    for i in num_arr:
        product *= int(i) 
    
    return product

def persistence(n):
    # your code
    count = 0
    num = n

    if len(str(n)) == 1:
           return 0
    
    while True:
         
         if len(str(num)) == 1:
              return count
         
         num = get_product(num)
         count += 1
         print(f"{num}")
    
    return count
      
# print(f"{persistence(4)}") # 0
# print(f"{persistence(39)}") # 3
# print(f"{persistence(99)}") # 2
# print(f"{persistence(999)}") # 4
print(f"{persistence(25)}") # 4