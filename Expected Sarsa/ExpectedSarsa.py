import blackjack
from pylab import *
import numpy as np
import random

numEpisodes = 10000000
returnSum = 0.0
epsilonu=0.19
epsilonpi=0.05
alpha = 0.001

Q=0.00001*np.random.rand(181,2)

"""
Returns the epsilonu greedy behaviour policy for given state
"""
def policy(state):
	testnumber=random.random()
	if (testnumber <= epsilonu):
		return random.randint(0,1)
	else:
		return np.argmax(Q[state])

"""
Returns the learned policy for given state
"""
def learnedPolicy(state):
	return np.argmax(Q[state])

"""
Returns the expected value for a given state
using epsisonpi greedy policy
"""	
def expectedValue(state):
	testnumber=random.random()
	if (state == -1):
		return 0
	elif (testnumber <= epsilonpi):
		return (0.5*Q[state][0] + 0.5*Q[state][1])
	else:
		return Q[state][np.argmax(Q[state])]


"""
Experiments:

First learn policy and calculate average return
"""

for episodeNum in range(numEpisodes):
	blackjack.init()
	state=0
	return1=0
	while (state != -1):
		action = policy(state)
		reward,statep=blackjack.sample(state,action) 
		Q[state][action] = Q[state][action] + alpha*(reward + expectedValue(statep) - Q[state][action])
		state = statep
		return1+=reward
	returnSum+=return1
	if (((episodeNum % 10000) == 0) and (episodeNum != 0)):
		print "Count =",episodeNum,"Average return: ", returnSum/(episodeNum)
	



blackjack.printPolicy(learnedPolicy)
print "Average return: ", float(returnSum)/float(numEpisodes)
returnSumLearned=0

"""
Now use learned policy and calculate average return
"""
for episodeNum in range(numEpisodes):
	blackjack.init()
	state=0
	return1=0
	while (state != -1):
		action = learnedPolicy(state)
		reward,statep=blackjack.sample(state,action) 
		state = statep+0
		return1+=reward
	returnSumLearned+=return1

print(returnSumLearned)
print(numEpisodes)
print "Average return learned: ", float(returnSumLearned)/float(numEpisodes)



