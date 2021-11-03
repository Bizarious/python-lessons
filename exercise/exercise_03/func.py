# Aufgabe 2
print("Aufgabe 2:")
# #1 Definiere eine Funktion, die 3 Variablen als Argumente nimmt.
# und True ausgibt, wenn 2 von 3 ebenfalls True sind.
# Probiere die Funktion aus.
def two_of_three(b1, b2, b3):
    return b1 and b2 or b1 and b3 or b2 and b3

# #2 Definiere eine Funktion, die die erste Funktion mit allen Möglichkeiten
# aufruft.
def alle_varianten():
    for b1 in [True, False]:
        for b2 in [True, False]:
            for b3 in [True, False]:
                result = two_of_three(b1, b2, b3)
                print(f"input: {[b1, b2, b3]} result: {result}")
alle_varianten()

# Aufgabe 3
print("Aufgabe 3:")
# #1 Definiere eine Funktion, die überprüft,
# ob eine Liste nur Zahlen enthält, die kleiner als 10 sind.
# Es soll entsprechend True oder False ausgegeben werden.
def liste_kleiner_zehn(zahlen):
    for zahl in zahlen:
        if zahl >= 10:
            return False
    return True
# Test
print(f" negativ Test: {liste_kleiner_zehn([2,3,1,3,4,5,10,1])}")
print(f" positiv Test: {liste_kleiner_zehn([2,3,1,3,4,5,6,1])}")

# #2 Definiere eine Funktion, die 2 Argumente annimmt (zahlen, teiler)
# und als Ergebnis eine neue liste zurückgibt, welche die originalen Zahlen
# geteilt durch den Teiler enthält. Teiler soll einen default Wert von 2 haben.
# Rufe die Funktion auf, mit und ohne das den teiler anzugeben.
# Beispiel: liste_teilen([4, 7, 16], 2) => [2, 3.5, 8]
def liste_teilen(zahlen, teiler=2):
    geteilte_zahlen = []
    for zahl in zahlen:
        geteilte_zahl = zahl / teiler
        geteilte_zahlen.append(geteilte_zahl)
    return geteilte_zahlen
# mit teiler angegeben
print(f"liste teilen, kein default {liste_teilen([3,15,11,15,78], 5)}")
# ohne teiler (wird als 2 behaldelt)
print(f"liste teilen, default {liste_teilen([3,15,11,15,78])}")

# #3 Definiere eine Funktion, die die beiden zuvor definierten Funktionen
# verwendet. Die Funktion soll, eine Liste von Zahlen solange durch 2 teilen,
# bis alle Zahlen der Liste kleiner als 10 sind und diese Liste dann ausgeben.
def liste_teilen_bis_kleiner_zehn(zahlen):
    while not liste_kleiner_zehn(zahlen):
        zahlen = liste_teilen(zahlen)
        print(f"geteilt: {zahlen}")
    return zahlen
print(f'teilen bis kleiner 10: {liste_teilen_bis_kleiner_zehn([342, 5253, 234, 234, 24])}')
