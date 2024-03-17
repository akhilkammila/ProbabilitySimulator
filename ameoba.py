import random

ameobas = 1
STOP = 1000
TRIALS = 1000

def runturn(ameobas):
    after = 0
    for i in range(ameobas):
        after += random.randint(0,3)
    return after

# returns True if we reach 0
def runsim():
    ameobas = 1
    while 0 < ameobas < STOP: ameobas = runturn(ameobas)
    return ameobas == 0

if __name__ == "__main__":
    hitzero = 0
    for i in range(TRIALS):
        hitzero += runsim()
    print(hitzero/TRIALS)