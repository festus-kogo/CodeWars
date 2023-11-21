s = "Hello"
print(list(s))
def remove_char(s):
    #your code here
    lst = list(s)
    lst.pop(0)
    lst.pop()

    return "".join(lst)

print(remove_char("Hello"))