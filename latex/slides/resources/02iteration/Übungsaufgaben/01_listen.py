# 1# erstelle leere liste
liste = []
print(f"1# leere liste: {liste}")

# 2# fülle die Liste nacheinander mit 13, 7, 0
liste.append(13)
liste.append(7)
liste.append(0)
print(f"2# gefüllte liste: {liste}")

# 3# addiere das erste und zweite Listenelement
# schreibe das Ergebniss in das dritte
liste[2] = liste[0] + liste[1]
print(f"3# nach Addition: {liste}")

# 4# entferne das 2. element der Liste
# und hänge es hinten wieder an die Liste
liste.append(liste.pop(1))
print(f"4# nach hinten anhängen: {liste}")

# ZUSATZ# überprüfe ob das 2. Elment kleiner ist als das dritte
# falls ja, füge an die Liste True an ansonsten False
liste.append(liste[0] < liste[1])
print(f"ZUSATZ# nach kleiner Check: {liste}")
