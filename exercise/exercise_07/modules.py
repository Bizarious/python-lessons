# 2.1
import time
import itertools

class Timer:

    def execute(self):
        t1 = time.time()
        self.action()
        t2 = time.time()
        return t2 - t1

    def action(self):
        pass

class SleepTimer(Timer):

    def action(self):
        time.sleep(3)

class NaiveLoop(Timer):

    def action(self):
        l = range(20)
        results = []
        for a in l:
            for b in l:
                for c in l:
                    for d in l:
                        for e in l:
                            results.append((a, b, c, d, e))
        print(len(results))

class EfficientLoop(Timer):

    def action(self):
        results = []
        for t in itertools.product(range(20), repeat=5):
            results.append(t)
        print(len(results))
        print(results)

# 2.2

if __name__ == "__main__":
    print(NaiveLoop().execute())
    print(EfficientLoop().execute())
