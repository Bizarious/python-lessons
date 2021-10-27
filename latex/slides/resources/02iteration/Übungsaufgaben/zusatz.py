# 2 Listen, deren Summe der Elemente gleich sind, bilden ein Paar
# Zähle für jede Teilliste, wieviele Paar-Partner vorhanden sind
number_lists = [[7, 4], [12, 1, 6], [9, 2], [5, 3, 3]]

equal_counter_list = []
for number_list_a in number_lists:
    equal_counter = -1
    for number_list_b in number_lists:
        if sum(number_list_a) == sum(number_list_b):
            equal_counter += 1
    equal_counter_list.append(equal_counter)
print(f"Ergebniss: {equal_counter_list}")
