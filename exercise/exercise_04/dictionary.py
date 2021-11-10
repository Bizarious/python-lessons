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
