# 1# Definiere eine funktion die zwei Punkte A,B entgegennimmt (als Tupel)
# und den Vector AB zurückgibt
def vector_zwischen(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1, y2 - y1)

A = (3, 5)
B = (-1, -2)
print(f"Vector zwischen {A} und {B}: {vector_zwischen(A, B)}")

# Erweitere die Funktion, sodass sie eingegebenen
# Vektoren beliebig viele Stellen haben können
def vector_zwischen(p1, p2):
    listen_vektor = [] #liste zum sammeln der Vectorteile
    for i in range(len(p1)):
        listen_vektor.append(p2[i] - p1[i])
    return tuple(listen_vektor) #Umwandlung der liste zum tuple

A = (1,0,4,7,2,4,5)
B = (1,2,3,9,2,5,6)
print(f"Vector zwischen {A} und {B}: {vector_zwischen(A, B)}")
