# https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python
# Welcome!

db = {
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'
}

# print(db)

def greet(language):
    # pass # your code here
    if language in db:
        return db[language]
    
    return 'Welcome'

print(greet('english')) # Welcome
print(greet('dutch')) # Welkom
print(greet('IP_ADDRESS_INVALID')) # Welcome
print(greet('')) # Welcome
print(greet(2)) # Welcome