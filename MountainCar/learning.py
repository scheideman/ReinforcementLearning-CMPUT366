#!/usr/bin/python
# -*- coding: utf-8 -*-
import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
from Tilecoder import numTiles as n
from pylab import *  # includes numpy
import copy

numRuns = 50
numEpisodes = 200
alpha = 0.5 / (numTilings)
gamma = 1
lmbda = .9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1] * numTilings
Q = [0] * 3
numActions = 3
returns = np.zeros([numRuns,numEpisodes])
stepList = np.zeros([numRuns,numEpisodes])
runList = np.zeros(numRuns)

runSum = 0.0
for run in xrange(numRuns):
    theta = -1*ones([numTiles,3]) #*rand(numTiles,3)
    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        step = 0
        e = np.zeros([numTiles,3])
        (position, velocity) = mountaincar.init()
        while 1: 
            tilecode(position, velocity, F)
            Q = np.sum(theta[F],axis=0) 

            if np.random.random() > epsilon:
                A = np.argmax(Q)
            else:
                A = np.random.randint(numActions)
     
            R, result = mountaincar.sample((position, velocity), A)
            error = R - Q[A]
            eOld = copy.copy(e)
            e[F,A] = 1
            G += R
            if result == None:
                theta = theta + alpha * error * e
                break

            newPosition,newVelocity = result
            oldF = copy.copy(F)
            tilecode(newPosition, newVelocity, F)
            
            Q = np.sum(theta[F],axis=0)

            error = error + (1 - epsilon) * np.max(Q) + epsilon \
                * np.average(Q) 
        
            theta = theta + alpha * error * e

            e = gamma*lmbda*eOld
            e[oldF,A] = 1

            position, velocity = newPosition, newVelocity
            step = step+1
        print 'Episode: ', episodeNum, 'Steps:', step, 'Return: ', G
        returnSum = returnSum + G
        stepList[run,episodeNum] = step
        returns[run,episodeNum] = G
    print 'Average return:', returnSum / numEpisodes
    runList[run] =  returnSum / numEpisodes
    runSum += returnSum
averageStep = np.average(stepList,axis=0)
averageReturn = np.average(returns,axis=0)
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
            Q = np.sum(theta[F],axis=0)
            height = -max(Q)
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

    fout = open('returnVal', 'w')
    fout1 = open('stepAvg', 'w')
    for i in range(numEpisodes):
        fout1.write(repr(averageStep[i]) + ' ')
        fout.write(repr(averageReturn[i]) + ' ')
    fout.close()
    fout1.close()

writeF()
stddev = np.std(runList)
stderror = stddev/np.sqrt(numRuns)
print("Mean performance", np.average(runList))
print("Standard Error",stderror)


		