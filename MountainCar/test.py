#!/usr/bin/python
# -*- coding: utf-8 -*-
import mountaincar
from Tilecoder import numTilings, tilecode, numTiles, setOffset
from Tilecoder import numTiles as n
from pylab import *  # includes numpy
import copy

numRuns = 1
numEpisodes = 200
alpha = 0.5 / numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1] * numTilings
Q = [0] * 3
numActions = 3

runSum = 0.0
for run in xrange(numRuns):
    #setOffset()  # maybe declare outside of loop
    theta = -0.01 * rand(numTiles,3)

    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        step = 0
        # your code goes here (20-30 lines, depending on modularity)
        e = np.zeros([numTiles,3])
        (position, velocity) = mountaincar.init()
        while 1:  # until terminal state is reached
            tilecode(position, velocity, F)

            #print("pos",position,"\n","velocity", velocity)
            # print("F",F)
            Q = np.sum(theta[F],axis=0) #inner product theta*phi, get state value for each action

            #print("Q",Q)
            #choose next action
            if np.random.random() > epsilon:
                A = np.argmax(Q)
            else:
                A = np.random.randint(numActions)
            #print ('A', A)
            R, result = mountaincar.sample((position, velocity), A)
            error = R - Q[A]
            eOld = copy.copy(e)
            e[F,A] = 1
            if result == None:
                print 'terminal'
                theta = theta + alpha * error * e
                break

            newPosition,newVelocity = result
            oldF = copy.copy(F)
            tilecode(newPosition, newVelocity, F)
            
            Q = np.sum(theta[F],axis=0)

            error = error + (1 - epsilon) * np.argmax(Q) + epsilon \
                * np.average(Q) 
                
            theta = theta + alpha * error * e

            tmp = np.zeros([numTiles,3])
            tmp[oldF,A] = 1
            e = np.maximum(lmbda*eOld,tmp)

            position, velocity = newPosition, newVelocity
            step = step+1
        print 'Episode: ', episodeNum, 'Steps:', step, 'Return: ', G
        returnSum = returnSum + G
    print 'Average return:', returnSum / numEpisodes
    runSum += returnSum
print 'Overall performance: Average sum of return per run:', runSum \
    / numRuns


# Additional code here to write average performance data to files for plotting...
# You will first need to add an array in which to collect the data

def writeF():
    fout = open('value', 'w')
    F = [0] * numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2 + i * 1.7 / steps, -0.07 + j * 0.14 / steps,
                     F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()



		