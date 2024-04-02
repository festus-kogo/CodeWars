# https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

def sum_str(a, b):
    # happy coding !
    print(f"a ==> {a}")
    print(f"b ==> {b}")

    if a == "" and b == "":
        return "0"
    
    elif b == "":
        return f"{a}"
    
    elif a == "":
        return f"{b}"
    
    return str( int(a) + int(b) )

# print(f"{sum_str('4','5')}")
# print(f"{sum_str('34','5')}")
# print(f"{sum_str('9','')}")
print(f"{sum_str('','')}")