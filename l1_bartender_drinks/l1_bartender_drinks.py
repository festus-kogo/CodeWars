# https://www.codewars.com/kata/568dc014440f03b13900001d/train/python

def get_drink_by_profession(param):
    # code me!
    data = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster Craft Beer", "Bike Gang Member": "Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}
    
    if param.title() in data:
        return data[param.title()]
    
    return "Beer"
