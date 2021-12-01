import my_modul
i = my_modul.MeineKlasse()

from my_modul import MeineKlasse
i = MeineKlasse()

if __name__ == "__main__":
    print("Wird nur ausgeführt, wenn dieses Script direkt aufgerufen wurde")

import time
# hält das Programm für 5s an
time.sleep(5)

import random
# Zufallszahl ziwschen 0 und 9
r = random.randint(0, 9)
