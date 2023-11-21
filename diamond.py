# https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python
# Give me a diamond

def diamond(n):
    # Make some diamonds!
    output = ""
    m = n * 2

    if n == 0 or n < 0 or n % 2 == 0:
        return None
    else:
        for i in range(1, (m + 1)):
            print(i)
            if i % 2 != 0:
                if i > n:
                    output += "*" * (m - i)                    
                    output += "\n"
                else:
                    output += "*" * i
                    output += "\n"

    return output
    
" *\n***\n *\n"
# print(diamond(0))   
# print(diamond(2))
# print(diamond(-3))
# print(diamond(1))
# print(diamond(3))
# print(diamond(5))
# diamond(1)
print(diamond(3))
# print(diamond(5))