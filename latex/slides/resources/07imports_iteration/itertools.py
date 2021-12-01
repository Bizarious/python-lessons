import itertools

# zweifach verschachtelt
numbers = [1, 2, 3, 4, 5, 6, 7]
for t in itertools.product(numbers, repeat=2):
    print(t)

for i in numbers:
    for j in numbers:
        t = (i, j)
        print(t)

# dreifach verschachtelt
numbers = [1, 2, 3, 4, 5, 6, 7]
for t in itertools.product(numbers, repeat=3):
    print(t)

for i in numbers:
    for j in numbers:
        for k in numbers:
            t = (i, j, k)
            print(t)
