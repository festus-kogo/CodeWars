# https://www.codewars.com/kata/56541980fa08ab47a0000040/python

def printer_error(s):
    # your codes
    a_m = "abcdefghijklm"
    count = 0

    for l in s:
        if l not in a_m:
            count += 1
    
    return f"{count}/{len(s)}"
        

print(printer_error("aaabbbbhaijjjm")) # 0/14

print(printer_error("aaaxbbbbyyhwawiwjjjwwm")) # 8/22