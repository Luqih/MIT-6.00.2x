import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    n = 1
    while (n % 2 != 0):
      n = random.randint(0, 99)
    return n

print(genEven())