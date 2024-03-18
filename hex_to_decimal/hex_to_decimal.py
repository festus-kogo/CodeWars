# https://www.codewars.com/kata/57a4d500e298a7952100035d/train/python
# https://www.rapidtables.com/convert/number/decimal-to-hex.html

def hex_to_dec(s):
    hex_dec = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}
    total = 0

    for i, j in enumerate(s[::-1]):
        if j.isalpha():
            total += int(hex_dec[j.upper()]) * 16 ** i
        else:
            total += int(j) * 16 ** i
    
    return total

# print(hex_to_dec("0")) # 0
# print(hex_to_dec("1")) # 1


def dec_hex(n):
    hex_dec_1 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    mod_1 = ""
    div = n

    while True:
        if div == 0:
            break

        div, mod = divmod(div, 16)
        if mod > 9:
            # print(f"div (decimal) => {div} mod (decimal) => {mod} mod (hex) => {hex_dec_1[mod]}")
            mod_1 += hex_dec_1[mod]
        else:
            # print(f"div (decimal) => {div} mod (decimal) => {mod} mod (hex) => {mod}")
            mod_1 += str(mod)
    
    return mod_1[::-1]

print(dec_hex(7562)) # 1D8A
print(dec_hex(35631)) # 8B2F


