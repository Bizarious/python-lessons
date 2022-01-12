# 1. Was macht die Funktion
def hello():
    print(hello)

# 2. Wert von x
lams= [lambda x: x**2, lambda x: x-1, lambda x: len(str(x))]
x = 10
for lam in list_of_objects:
    x = lam(x)

# 3. Ist x ein(e)
def combination_function(func_one, func_two):
    def new_function(zahl):
        zahl = func_one(zahl)
        zahl = func_two(zahl)
        return zahl
    return new_function

x = combination_function(lambda x: x+5, lambda x: x*2)
