def first():
    with open("test.txt", "r+") as f:
        s = f.read()
        s_new = "".join("abc" if i == "a" else "bb" for i in s)
        f.seek(0)
        f.write(s_new)


def second():
    with open("test.txt", "r+") as f:
        d = {"a": "abc", "b": "bb", "c": "cac"}
        s = f.read()
        s_new = "".join(d[i] for i in s)
        f.seek(0)
        f.write(s_new)

