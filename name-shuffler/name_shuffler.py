# https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python

def name_shuffler(str_):
    count = len(str_.split())
    arr = []

    while count > 0:
        arr.append(str_.split()[count - 1])
        count -= 1
    
    return " ".join(arr)

print(name_shuffler("john McClane")) # McClane john
print(name_shuffler("john Doe")) # Doe john
print(name_shuffler("Festus Kogo")) # Kogo Festus