from inheritance import PKW, LKW, Panzer

l = [PKW(4), LKW(5)]
for i in l:
    print(i.info())

p = Panzer(3)
for i in range(4):
    p.schiessen()
