# Iteration über eine range
for i in range(1000):
    print(i)

# Iteration über eine Liste
cities = ['Tokio', 'Rio', 'Denver', 'Berlin', 'Nairobi', 'Moskau', 'Helsinki', 'Oslo']
for city in cities:
    print(city)

# Iteration über String
for letter in 'abcdefg':
    print(letter)

# Iteration über die Länge einer Liste
for i in range(len(cities)):
    city = cities[i]
    print(f"index: {i}, stadt: {city}")
