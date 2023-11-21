# https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python
# Twice as old

def twice_as_old(dad_years_old, son_years_old):
    # pass
    return abs((2 * son_years_old) - dad_years_old)

print(twice_as_old(36,7)) # 22
print(twice_as_old(55,30)) # 5
print(twice_as_old(42,21)) # 0
print(twice_as_old(22,1)) # 20
print(twice_as_old(29,0)) # 29