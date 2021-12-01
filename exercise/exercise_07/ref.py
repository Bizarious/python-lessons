class Example:
    def __init__(self, x):
        self.x = x

a = Example(0)
d = {"a": a}
a.x = 2
b = d["a"].x

a = [1, 2]
a.append(a)
b = a[2][2][2][2][2][2][2][2][0]
