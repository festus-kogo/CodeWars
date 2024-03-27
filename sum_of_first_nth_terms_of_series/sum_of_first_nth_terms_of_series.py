# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

def series_sum(n):
    # Happy Coding ^_^
    sum_total = 0
    denom = 4

    if n == 1:
        return "1.00"
    
    for i in range(1, n + 1):        
        # print(f"i is at {i}")
        if i == 1:
            sum_total += 1.00
        else:
            sum_total += 1 / denom
            denom += 3
    
    return f"{sum_total:.2f}"
        



print(f"{series_sum(1)}")
print(f"{series_sum(2)}")
print(f"{series_sum(3)}")
print(f"{series_sum(5)}")
