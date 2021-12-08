import time

def hallo():
    print("Hallo Welt")
    return 100

def zeit_messen(action):
    t1 = time.time()

    action()

    t2 = time.time()
    print(t2 - t1)

zeit_messen(hallo)

print(hallo()) # 100
print(hallo)   # <function hallo at 0x7fa0353a30d0>
