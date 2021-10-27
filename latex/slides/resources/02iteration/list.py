# eine Liste initialisieren
prime_list = [2, 3, 5, 7, 11, 13]

# Listen können jegliche Objekte,
# auch gemischt und mehrfach enthalten
stuff = [5, 1.56363, 5, False, prime_list, None, False]

# einzelne Elemente referenzieren
first_prime = prime_list[0] #2
third_prime = prime_list[2] #5
last_prime = prime_list[-1] #13
# Elemente zu schreiben ist auch möglich
prime_list[0] = 42

# neue Elemente anfügen
prime_list.append(15)
print(prime_list) #[2, 3, 5, 7, 11, 13, 15]

# Elemente entfernen
prime_list.remove(11)
print(prime_list) #[2, 3, 5, 7, 13, 15]

# Elemente per Index entfernen
last_prime = prime_list.pop() #13
print(prime_list) #[2, 3, 5, 7, 11]
