buchstaben = ['A', 'B', 'C', 'D']

for index, buchstabe in enumerate(buchstaben):
    # index 0, buchstabe 'A'
    # index 1, buchstabe 'B'
    # ...
    pass

for tuple_element in enumerate(buchstaben):
    # tuple_element (0, 'A')
    # tuple_element (1, 'B')
    # ...
    pass

b_klein = ['a', 'b', 'c', 'd']
b_gross = ['A', 'B', 'C', 'D']
for klein, gross in zip(b_klein, b_gross):
    # klein 'a', gross 'A'
    # klein 'b', gross 'B'
    # ...
    pass

for tuple_element in zip(b_klein, b_gross):
    # tuple_element ('a', 'A')
    # tuple_element ('b', 'B')
    # ...
    pass


vornamen = ["Hans", "Lisa", "Steffen"]
mittelnamen = ["Günther", "", "G."]
nachnamen = ["Schulze", "Klein", "Südmann"]

for vorname, mittelname, nachname in zip(vornamen, mittelnamen, nachnamen)
    name = vorname + mittelname + nachname
    print(name)
