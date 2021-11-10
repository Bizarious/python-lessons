def get_type_name(o):
    return o.__class__.__name__

# 2.1. Dictionary mit verschiedenen Typen

def sort_types(types):
    d = {}
    for t in types:
        d[t] = get_type_name(t)
    return d

a = sort_types([2, "5", True, False, "6", 42, None])
print(a)

# 2.2.
def sort_types_2(types):
    d = {}
    for t in types:
        name = get_type_name(t)
        if name not in d:
            d[name] = []
        d[name].append(t)
    return d

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

print(count_values({1: True, "lksajd": False, None: "ad", 5: 42, "sad": "lsakdjl", 92: 42}))

# 3.2.
def get_max(d):
    max_key, max_value = None, 0
    for key in d:
        if d[key] >= max_value:
            max_key, max_value = key, d[key]
    return max_key

print(get_max({"x": 1, "y": 4, "z": 2}))



# 3.Zusatz
def calculate_sums(input_list):
    cache = {}
    output = []
    for a,b in input_list:
        if (a,b) in cache.keys():
            print("answer from cache")
            output.append(cache[(a,b)])
        else:
            result = a + b
            output.append(result)
            cache[(a,b)] = result
    print(f"finaler cache Zustand: {cache}")
    return output

input_list = [(1, 2), (65, 7), (4, 5), (65, 7)]
calculate_sums(input_list)



