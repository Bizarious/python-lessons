# Lösungen für "Tupel und Dictionary"
# Aufgabe 1

#### Schreibe eine Funktion, die zwei 2-dimensionale Punkte A und B ####
#### (jeweils als Tupel) entgegennimmt und den Vektor AB ####
#### als Tupel zurückgibt. ####

def vector_zwischen(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1, y2 - y1)

A = (3, 5)
B = (-1, -2)
print(f"Vector zwischen {A} und {B}: {vector_zwischen(A, B)}")

#### Modifiziere die Funktion so, dass sie nun Vektoren ####
#### beliebiger Dimension berechnen kann. Der Einfachheit halber ####
#### gehen wir davon aus, dass beide Punkte die selbe Dimension haben. ####

def vector_zwischen(p1, p2):
    listen_vektor = [] #liste zum sammeln der Vectorteile
    for i in range(len(p1)):
        listen_vektor.append(p2[i] - p1[i])
    return tuple(listen_vektor) #Umwandlung der liste zum tuple

A = (1,0,4,7,2,4,5)
B = (1,2,3,9,2,5,6)
print(f"Vector zwischen {A} und {B}: {vector_zwischen(A, B)}")
