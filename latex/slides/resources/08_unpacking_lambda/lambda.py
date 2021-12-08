def map(funktion, liste):
    out = []
    for element in liste:
        neues_element = funktion(element)
        out.append(neues_element)
    return out

numbers = [1, 2, 3, 4, 5, 6]
numbers = map(lambda x: x**2, numbers)
print(numbers) # [1, 4, 9, 16, 25, 36]
