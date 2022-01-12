# Standardweg
liste = []
for i in range(5):
    liste.append(i)

# list comprehension
liste = [i for i in range(5)]

fruits = ["apple", "avocado", "banana", "strawberry", "raspberry"]
filt = [fruit for fruit in fruits if fruit.startswith("a")]
# ['apple', 'avocado']

filt = [fruit if fruit.startswith("a") else "IIIHHH, eine Frucht ohne A!" for fruit in fruits]
# ['apple', 'avocado', 'IIIHHH, eine Frucht ohne A!', 'IIIHHH, eine Frucht ohne A!', 'IIIHHH, eine Frucht ohne A!']

nested = [["a", "b"], [1, 2, 3]]
multiple = [i for sub in nested for i in sub]
# ['a', 'b', 1, 2, 3]
