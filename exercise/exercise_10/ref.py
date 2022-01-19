d = {"a": lambda x: x*2, "b": lambda y, z: y(z)}
print(d["b"](d["a"], 4))

def rec(depth):
    if depth <= 1:
        return 1
    return rec(depth-1) + rec(depth-2)

for i in range(5):
    print(rec(i))
