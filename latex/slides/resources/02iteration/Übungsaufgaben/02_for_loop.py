# 1# erstelle eine leere liste und fülle sie
# mit den Zahlen von 1 bis 100
numbers = []
for i in range(100):
    numbers.append(i + 1)

print(f"1# 1 bis 100 liste: {numbers}")

# 2# addiere alle Zahlen in der Liste auf eine neue Variable
complete_sum = 0
for number in numbers:
    complete_sum += number

print(f"2# summe: {complete_sum}")
# 3# Erstelle 2 neue leere Listen für gerade und ungerade Zahlen.
# iteriere durch die originale Liste und ordne die Elemente den
# Teillisten zu.

even = []
odd = []
for number in numbers:
    if number % 2:
        odd.append(number)
    else:
        even.append(number)

print(f"3# gerade: {even},\nungerade: {odd}")
