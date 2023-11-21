# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Happy Coding! ;)
    if (fuel_left * mpg) >= distance_to_pump:
        return True
    
    return False

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))