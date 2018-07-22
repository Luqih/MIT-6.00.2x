import random

def drawBall(balls):
    pos = random.randint(0, len(balls) - 1)
    item = balls[pos]
    del balls[pos]
    return [item, balls]

def noReplacementSimulation(numTrials):
    total = 0
    for trial in range(numTrials):
        balls = ['R', 'R', 'R', 'G', 'G', 'G']
        drawedBalls = []
        for ball in range(3):
            item, balls = drawBall(balls)
            drawedBalls.append(item)
        if (drawedBalls[0] == drawedBalls[1] and drawedBalls[0] == drawedBalls[2]):
            total += 1
    return total / numTrials
        
    
print(noReplacementSimulation(2000000))