def gerade(number):
    return int(number) % 2 == 0

def teilbar_durch(dividend, divisor):
    return int(dividend) % int(divisor) == 0

def multiplizieren(number, *multiplier):
    result = []
    for m in multiplier:
        result.append(int(number)*int(m))
    return result

while True:
    i = input("Befehl eingeben: ")
    cmd, *args = i.split(" ")

    if cmd == "gerade":
        print(gerade(*args))
    elif cmd == "teilbar":
        print(teilbar_durch(*args))
    elif cmd == "mult":
        print(multiplizieren(*args))
