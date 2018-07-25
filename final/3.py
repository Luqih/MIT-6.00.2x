import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    choices = np.array(choices)
    choicesLn = len(choices)
    attempt = np.array(choices * 0)
    results = []

    while not len(results):
        for i in range(0, 2 ** choicesLn + 1):
            binary = bin(i)[2:].zfill(choicesLn)[:choicesLn]
            attempt = np.array(list(map(int, binary)))
            if sum(attempt * choices) == total:
                results.append(attempt)
        if not len(results):
            total -= 1
        else:
            break

    bestResultIndex = 0
    for index, result in enumerate(results):
        if sum(results[bestResultIndex]) > sum(result):
            bestResultIndex = index
    return results[bestResultIndex]

print(find_combination([4, 6, 3, 5, 2], 10))