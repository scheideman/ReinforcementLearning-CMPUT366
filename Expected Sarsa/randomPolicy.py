import blackjack
from pylab import *
import numpy as np
import random

numEpisodes = 2000
returnSum = 0.0

"""
Returns equiprobable random policy
"""
def policy():
    return random.randint(0,1)	

"""
Experiment
"""
for episodeNum in range(numEpisodes):
    G = 0
    state=0
    blackjack.init()
    while (state != -1):
        returntuple=blackjack.sample(state,policy()) 
    	reward=returntuple[0]
	state=returntuple[1]
	G += reward
    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes

