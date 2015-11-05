import blackjack
from pylab import *
import numpy as np
import random
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

numEpisodes = 10000000
returnSum = 0.0
epsilonu=0.19
epsilonpi=0.005
alpha = 0.001
#logfile= open("logfile.csv","a")
#writer=csv.writer(logfile)

Q=0.00001*np.random.rand(181,2)

#print(Q)
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

def plotter():
	X = np.zeros(90)
	Y = np.zeros(90)
	Z = np.zeros(90)
	for s in np.arange(1,90):
		blackjack.decode(s)
		X[s] = blackjack.dealerCard
		Y[s] = blackjack.playerSum
		Z[s] = max(Q[s])

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(X, Y, Z, c='r', marker='o')
	ax.set_ylim(12, 20)
	plt.show()


"""
First learn policy and calculate average return
"""
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
		state = statep
		return1+=reward
	returnSum+=return1
blackjack.printPolicy(learnedPolicy)
print "Average return: ", float(returnSum)/float(numEpisodes)
returnSumLearned=0

"""
Now use learned policy and calculate average return
"""
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

print(returnSumLearned)
print(numEpisodes)
print "Average return learned: ", float(returnSumLearned)/float(numEpisodes)

plotter()
"alpha","epsilonu","epsilonpi","average return","learned average return","number of episodes"
#writer.writerow((alpha,epsilonu,epsilonpi,float(returnSum)/float(numEpisodes),float(returnSumLearned)/float(numEpisodes),numEpisodes))

#logfile.close()

