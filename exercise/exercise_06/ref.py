a = []
b = [1]
a.append(b)
a.append(b)
b.append(5)
print(a)

def f(liste):
    liste.remove(1)

a = [1, 2, 3]
f(a)
print(a)

def f(liste):
    l = liste[:]
    l.remove(5)
    return l

a = [4, 5, 6]
b = f(a)
print(a)
print(b)
