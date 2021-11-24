class Baum:
    def __init__(self, alter, hoehe):
        self.alter = alter
        self.hoehe = hoehe

    def wachsen(self, hoehe):
        self.hoehe += hoehe

class NadelBaum(Baum):
    pass

nadelbaum1 = NadelBaum(15, 20)
nadelbaum1.wachsen(5)
print(nadelbaum1.hoehe) # 25

class NadelBaum(Baum):
    def __init__(self, alter, hoehe, laenge_nadeln):
        super().__init__(alter, hoehe)
        self.laenge_nadeln = laenge_nadeln

    def wachsen(self, hoehe):
        super().wachsen(hoehe)
        print(f"um {hoehe} gewachsen")
        self.laenge_nadeln += hoehe * 0.01

nadelbaum1 = NadelBaum(15, 20, 0.5)
nadelbaum1.wachsen(5)
print(nadelbaum1.laenge_nadeln)
