class Tier:
    def macht(self):
        print("ein Geräusch")

class Kuh(Tier):
    def macht(self):
        print("muh!")

class Schwein(Tier):
    def macht(self):
        print("oink!")

tiere = [Kuh(), Schwein(), Schwein(), Kuh(), Kuh()]
for tier in tiere:
    tier.macht()
