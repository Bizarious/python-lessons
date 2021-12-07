(a, b, c) = (1, 2, 3)
# oder
a, b, c = (1, 2, 3)
# oder
a, b, c = 1, 2, 3

*a, = 1, 2, 3
# a = [1, 2, 3]

a*, b = 1, 2, 3
# a = [1, 2], b = 3
a, *b = 1, 2, 3
# a = 1, b = [2, 3]
a, *b, c = 1, 2, 3, 4, 5
# a = 1, b = [2, 3, 4], c = 5
*a, b, c, d = 1, 2, 3, 4, 5
# a = [1, 2], b = 3, c = 4, d = 5

def func(*args):
    print(args)

func(42, 1337, True, None, "Hello")
# gibt (42, 1337, True, None, "Hello") aus

def func(a, b, c):
    print(f"{a}, {b}, {c}")

func(*(False, "Hi", 8))
# gibt "False Hi 8" aus

def func(*args):
    print(args)

func(*(False, "Hi", 8))
# gibt (False, "Hi", 8) aus

def func(**kwargs):
    print(kwargs)

func(var_1=42, var_2="Hello World", var_3=True)
# gibt {var_1: 42, var_2: "Hello World", var_3=True aus}

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, wert_1=None, wert_2=1337)
# args ist (1, 2)
# kwargs ist {wert_1: None, wert_2: 1337}
