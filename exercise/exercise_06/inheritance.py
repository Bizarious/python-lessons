# 2.1, 2.2
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

# 2.3, 2.4
class LKW(Fahrzeug):

    def __init__(self, laderaum):
        super().__init__(200000, 80)
        self.laderaum = laderaum

    def hupen(self):
        print("HUUUUUP!")

    def info(self):
        return super().info() + f" Laderaum: {self.laderaum}"

class PKW(Fahrzeug):

    def __init__(self, personen_zahl):
        super().__init__(30000, 180)
        self.personen_zahl = personen_zahl

    def info(self):
        return super().info() + f" Personenzahl: {self.personen_zahl}"

# Z.
class Panzer(Fahrzeug):

    def __init__(self, anzahl_munition):
        super().__init__(6000000, 70)
        self.anzahl_munition = anzahl_munition

    def schiessen(self):
        if self.anzahl_munition > 0:
            print("Feuer!")
            self.anzahl_munition -= 1
        else:
            print("Keine Munition!")

    def info(self):
        return super().info() + f" Munition: {self.anzahl_munition}"
