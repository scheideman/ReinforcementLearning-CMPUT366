import blackjack
from pylab import *
import numpy as np
import random
#import pdb

numEpisodes = 1000000
returnSum = 0.0
epsilonu=0.01
epsilonpi=0.01
alpha = 0.001

Q = [[0.000001*random.random() for x in range(2)] for x in range(181)]


"""
policy() returns equiprobable random policy
"""
def policy(state):
	testnumber=random.random()
	if (testnumber <= epsilonu):
		return random.randint(0,1)
	else:
		return np.argmax(Q[state])

def learnedPolicy(state):
	#pdb.set_trace()
	return np.argmax(Q[state])
			
def expectedValue(state):
	testnumber=random.random()
	if (state == -1):
		return 0
	elif (testnumber <= epsilonpi):
		return (0.5*Q[state][0] + 0.5*Q[state][1])
	else:
		return Q[state][np.argmax(Q[state])]
		
count=0
for episodeNum in range(numEpisodes):
	count+=1
	blackjack.init()
	state=0
	return1=0
	while (state != -1):
		action = policy(state)
		reward,statep=blackjack.sample(state,action) 
		Q[state][action] = Q[state][action] + alpha*(reward + expectedValue(statep) - Q[state][action])
		state = statep +0
		return1+=reward
	returnSum+=return1
blackjack.printPolicy(learnedPolicy)

	
"""
	if ((episodeNum % 10000) == 0):
		print(count,"Average return: ", returnSum/(episodeNum+1))
	
print "Average return: ", returnSum/numEpisodes
"""
