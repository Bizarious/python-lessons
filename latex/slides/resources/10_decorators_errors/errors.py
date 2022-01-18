liste = [0]
try:
    print(liste[1])
except:
    print("Da war ein Fehler")

try:
    # irgendwelcher Code
except ValueError:
    print("Ein ValueError")
except ZeroDivisionError:
    print("Man darf nicht durch Null teilen")
except IndexError:
    print("Dieser Index exisitert nicht")

try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)
# printet "division by zero" aus

try:
    print(1/0)
except Exception as e:
    print(e)
# division by zero

try:
    print(1/0)
except ZeroDivisionError:
    print("Man darf nicht durch Null teilen")
finally:
    print("Fertig")
# printet "Man darf nicht durch Null teilen" und danach "Fertig" aus

try:
    raise RuntimeError("Ein Error zum Testen")
except Exception as e:
    print(e)
# printet "Ein Error zum Testen" aus
