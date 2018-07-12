import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    n = 1
    while (n % 2 != 0):
      n = random.randint(9, 21)
    return n
