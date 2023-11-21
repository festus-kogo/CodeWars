# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python

# The Feast of Many Beasts

def feast(beast, dish):
    # your code here
    if list(beast)[0] == list(dish)[0] and list(beast)[-1] == list(dish)[-1]:
        return True
    
    return False


print(feast("great blue heron", "garlic naan"))
print(feast("chickadee", "chocolate cake"))
print(feast("chickadeew", "chocolate cake"))