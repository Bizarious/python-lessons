# Lösungen für "Tupel und Dictionary"
# Aufgabe 2

# die Hilfsfunktion, um den Typen einer Variable als String zu bekommen.
def get_type_name(o):
    return o.__class__.__name__

#### 1.  Es ist eine Liste von Variablen verschiedener Typen gegeben. ####
#### Schreibe eine Funktion, die ein Dictionary zurück gibt, ####
#### in dem die Variablen als Keys verwendet werden ####
#### und ihr jeweiliger Typ als Value. ####

def sort_types(types):
    d = {}
    for t in types:
        # wir iterieren durch die Liste "types" und fügen den Wert als Key,
        # sowie seinen Typen als dazugehörigen Value in das Dictionary "d".
        d[t] = get_type_name(t)
    return d

a = sort_types([2, "5", True, False, "6", 42, None])
print("# 2.1:")
print(a)

#### 2. Definiere eine zweite Funktion, die stattdessen den Typ ####
#### einer Variable als Key verwendet. Alle Variablen eines Typs sollen, ####
#### in einer Liste als Value für den jeweiligen Key, abgespeichert werden. ####

def sort_types_2(types):
    d = {}
    for t in types:
        name = get_type_name(t)
        # wir wissen nicht, ob der Key und die dazugehörige Liste im Dictionary
        # bereits existiert. Daher müssen wir prüfen, ob der Key schon da ist.
        # Das kann man mit "name not in d" machen, was True zurückgibt, Wenn
        # die Variable "name" noch nicht als Key existiert. Alternativ kann man
        # auch "name not in d.keys()" schreiben.
        if name not in d:
            d[name] = []
        d[name].append(t)
    return d

print("# 2.2:")
print(sort_types_2([42, "as", 2, 3, "df", True, None, False, True, None]))

# 3.1.
def count_values(d):
    count = {}
    for i in d:
        if d[i] not in count.keys():
            count[d[i]] = 1
        else:
            count[d[i]] += 1
    return count

print("# 3.1:")
print(count_values({1: True, "lksajd": False, None: "ad", 5: 42, "sad": "lsakdjl", 92: 42}))

# 3.2.
def get_max(d):
    max_key, max_value = None, 0
    for key in d:
        if d[key] >= max_value:
            max_key, max_value = key, d[key]
    return max_key

print("# 3.2:")
print(get_max({"x": 1, "y": 4, "z": 2}))



# 3.Zusatz
def calculate_sums(input_list):
    cache = {}
    output = []
    for a,b in input_list:
        if (a,b) in cache.keys():
            print(f"answer from cache for {(a,b)}")
            output.append(cache[(a,b)])
        else:
            result = a + b
            output.append(result)
            cache[(a,b)] = result
    print(f"finaler cache Zustand: {cache}")
    return output

input_list = [(1, 2), (65, 7), (4, 5), (65, 7)]
print("# 3.Z:")
print(f"result sums: {calculate_sums(input_list)}")
