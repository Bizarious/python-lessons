# Initialisierung mit ()
tuple_eins = (1, True, 4.5, "hallo")

# Elemente abfragen wie bei Listen
viereinhalb = tuple_eins[2] #4.5
hallo = tuple_eins[-1] #'hello'
vordere = tuple_eins[:2] #(1, True)

# Elemente verändern, unmöglich !
tuple_eins[0] = "neuer Wert" #TypeError
# Ganzes Tuple austauschen, möglich !
tuple_eins = ("neuer Wert", True, 4.5, "hallo")

# mehrere Werte gleichzeitig abfragen
positions_tuple = (45.65, 198.12)
(x, y) = positions_tuple # x: 45.65, y: 198.12

# unter anderem nützlich für startwerte
(x, y, z) = (0, 100, 200) #x: 0, y: 100, z:200
