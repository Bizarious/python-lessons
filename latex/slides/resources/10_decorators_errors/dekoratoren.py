
def beispiel_dekorator(func):
    def ausgabe_funktion(x, y, z=0):
        func(x, y)
        print(z)
    return ausgabe_funktion

@beispiel_dekorator
def test(x, y):
    print(f"test {x} {y}")

def test(x, y):
    print(f"test {x} {y}")

test = beispiel_dekorator(test)


triggers = []

def always_run(func):
    triggers.append(func)
    return func

@always_run
def hello():
    print("hello")

while(True):
    inp = input("Wort eingeben:")
    for t in triggers:
        t()

def deko_eins(func):
    def out():
        func()
        print("deko eins")
    return out


def deko_eins(func):
    def out():
        print("deko eins start")
        func()
        print("deko eins ende")
    return out

def deko_zwei(func):
    def out():
        print("deko zwei start")
        func()
        print("deko zwei ende")
    return out

@deko_eins
@deko_zwei
def hi():
    print("hi")

hi()

hi = deko_zwei(hi)
hi = deko_eins(hi)
