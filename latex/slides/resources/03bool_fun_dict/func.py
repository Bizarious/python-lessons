def my_funtion():
    print("Dies ist eine Funktion")

# irgendwo im Programmablauf
my_function()

# beliebig viele Argumente mit Komma getrennt in die Klammern
def potenz(x, y):
    print(x**y)

# Argumente werden in der Reihenfolge belegt, wie sie angegeben wurden
potenz(2, 3) # x = 2, y = 3

def potenz(x, y):
    # x^y wird zurückgegeben
    return x**y

p = potenz(2, 3) # p = 8

def potenz(x, y=2):
    return x**y

p = potenz(2) # p = 4
p = potenz(2, 3) # p = 8
