def aktion(argument_1, argument_2="Y", argument_3="Z"):
    print(f"{argument_1} {argument_2} {argument_3}")

aktion("X")
aktion("X", "Y", "Hallo")
aktion("X", argument_3="Hallo")

def aktion(argument_1, *, argument_2, argument_3):
    print(f"{argument_1} {argument_2} {argument_3}")

aktion("X", argument_2="Y", argument_3="Z")
