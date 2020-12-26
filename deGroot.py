
import numpy as np


def deGroot(environment, beliefs):
    i = 0
    consensus = False
    while (consensus == False and i < 1000):
        old_beliefs = beliefs
        beliefs = environment @ beliefs
        if (np.all(old_beliefs - beliefs == np.zeros(len(beliefs)))):
            consensus = True
        i = i + 1
    return beliefs


def deGrootSteps(environment, beliefs):
    steps = []
    i = 0
    consensus = False
    while (consensus == False and i < 1000):
        old_beliefs = beliefs
        beliefs = environment @ beliefs
        if (np.all(old_beliefs - beliefs == np.zeros(len(beliefs)))):
            consensus = True
        i = i + 1
        steps.append(beliefs)
    return steps


#print(deGroot(T, p0))
