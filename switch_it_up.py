# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
# Switch it Up!

def switch_it_up(number):
    #your code here
    match number:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5: 
            return "Five"
        case 6:
            return "Six"
        case 7:
            return "Seven"
        case 8:
            return "Eight"
        case 9:
            return "Nine"
        case _:
            print("Something went wrong!")

    return number

print(switch_it_up(0))
print(switch_it_up(9))