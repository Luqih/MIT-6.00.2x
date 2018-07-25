import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 30
CURRENTFOXPOP = 500

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    if CURRENTRABBITPOP < 10:
        return

    newRabbits = 0
    repProb = 1 - CURRENTRABBITPOP / MAXRABBITPOP
    for rabbit in range(0, CURRENTRABBITPOP):
        if random.random() <= repProb:
            newRabbits += 1
    n = newRabbits + CURRENTRABBITPOP
    CURRENTRABBITPOP = n if n < 1000 else 1000
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    if CURRENTRABBITPOP < 10 or CURRENTFOXPOP < 10:
        return

    eatProb = CURRENTRABBITPOP / MAXRABBITPOP
    eatenRabbits = 0
    foxesChange = 0
    for fox in range(0, CURRENTFOXPOP):
        if random.random() <= eatProb:
            eatenRabbits += 1
            if random.random() <= 1/3:
                foxesChange += 1
        else:
            if random.random() <= 1/10:
                foxesChange -= 1
    n = CURRENTRABBITPOP - eatenRabbits
    CURRENTRABBITPOP = n if n > 10 else 10
    n = CURRENTFOXPOP + foxesChange
    CURRENTFOXPOP = n if n > 10 else 10
            
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []
    
    for step in range(0, numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)


rabbitPopulationOverTime, foxPopulationOverTime = runSimulation(200)

#pylab.plot(rabbitPopulationOverTime)
#pylab.plot(foxPopulationOverTime)

coeff = pylab.polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbitPopulationOverTime))))

coeff = pylab.polyfit(range(len(foxPopulationOverTime)), foxPopulationOverTime, 2)
pylab.plot(pylab.polyval(coeff, range(len(foxPopulationOverTime))))