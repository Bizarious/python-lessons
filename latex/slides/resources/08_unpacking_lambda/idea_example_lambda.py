def wrapper(funktion):
    print(funktion())

wrapper(lambda: "Hallo")

wrapper(
    def meine_funktion():
        return "Hallo"
)
