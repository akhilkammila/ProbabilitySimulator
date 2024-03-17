"""
what is the exp. difference between two nums 10-99

dif of 0: 100
dif of 1: 99
dif of 2: 98
dif of 99: 1
"""

def dif(n):
    answ = 0
    nums = 0

    for dif in range(0, 99-10+1):
        answ += dif * (90-dif)
        nums += 90-dif
    
    return answ / nums


if __name__ == "__main__":
    print(dif(100))