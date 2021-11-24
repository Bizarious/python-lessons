from inheritance import Fahrzeug


fahrzeuge = [Fahrzeug(1000, 10), Fahrzeug(20000, 100)]

for fahrzeug in fahrzeuge:
    print(fahrzeug.info())
    fahrzeug.fahren(100)
    fahrzeug.hupen()
