a = "Hallo"
b = a
b += " Welt"

a = [1, []]
a[0] + 1
a[1].append(1)

a = [42, ["hi"], (1, 5)]
b = a[:]
b.append(True)
b[1].append(False)
b[0] = 5

a = {"liste": [1, 2]}
b = a["liste"][:]
a["liste"].append(3)
b.remove(2)
