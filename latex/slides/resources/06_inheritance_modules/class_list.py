class Fahrzeug:
    def __init__(self, preis, speed):
        self.preis = preis
        self.speed = speed

    def hupen(self):
        print("Huuup!")

    def fahren(self, dauer):
        print("fahren")
        return dauer * self.speed

    def info(self):
        return f"Preis: {self.preis} €, Speed: {self.speed} km/h"


fahrzeuge = [Fahrzeug(1000, 10), Fahrzeug(20000, 100)]

for fahrzeug in fahrzeuge:
    print(fahrzeug.info())
