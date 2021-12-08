def test(*args, **kwargs):
    func, *rest = args
    r = func(**kwargs)
    for f in rest:
        r = f(r)
    return r

print(test(lambda x, y: (x+y, x*y), lambda a: a[0]+a[1], y=3, x=2))


while True:
    i = input().split(" ")
    sorted_list = sorted(i, key=lambda x: len(x))
    print(sorted_list)
