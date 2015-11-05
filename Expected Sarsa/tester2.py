import blackjack
from pylab import *
import numpy as np
import random
import csv


numEpisodes = 1000000
returnSum = 0.0
epsilonu=0.19
epsilonpi=0.01
alpha = 0.1


logfile= open("logfile.csv","a")

writer=csv.writer(logfile)


Q=0.00001*np.random.rand(181,2)

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
eu  = [0.5,0.5,0.1]
epi = [0,0.001,0.01]

for i in range(0,80):
	returnSum=0.0
	alpha = 0.001
	epsilonu = 0.19
	if (i<20):
		epsilonpi = 0.05
	elif (i<40):
		epsilonpi = 0.005
	elif (i<60):
		epsilonpi = 0.0005
	elif (i<80):
		epsilonpi = 0


	for episodeNum in range(numEpisodes):
		count+=1
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
	#blackjack.printPolicy(learnedPolicy)
	#print "Average return: ", float(returnSum)/float(numEpisodes)
	returnSumLearned=0.0

	for episodeNum in range(numEpisodes):
		count+=1
		blackjack.init()
		state=0
		return1=0
		while (state != -1):
			action = learnedPolicy(state)
			reward,statep=blackjack.sample(state,action) 
			state = statep+0
			return1+=reward
		returnSumLearned+=return1

	
	#print "Average return learned: ", float(returnSumLearned)/float(numEpisodes)

	writer.writerow((alpha,epsilonu,epsilonpi,float(returnSum)/float(numEpisodes),float(returnSumLearned)/float(numEpisodes),numEpisodes))

logfile.close()

