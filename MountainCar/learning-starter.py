import mountaincar
from Tilecoder import numTilings, tilecode, numTiles, setOffset
from Tilecoder import numTiles as n
from pylab import *  #includes numpy

numRuns = 1
numEpisodes = 200
alpha = 00.5/numTilings
gamma = 1
lmbda = 0.9
Epi = Emu = epsilon = 0
n = numTiles * 3
F = [-1]*numTilings
Q = [0]*3
numActions = 3


runSum = 0.0
for run in xrange(numRuns):
    setOffset()  # maybe declare outside of loop 
    theta = -0.01*rand(n)

    returnSum = 0.0
    for episodeNum in xrange(numEpisodes):
        G = 0
        #your code goes here (20-30 lines, depending on modularity)
        e = zeros(n)
        position, velocity = mountaincar.init()
        while(1): #until terminal state is reached 
            tilecode(position,velocity,F)     
            for a in range(3):
                i = a*4*9*9
                Q[a] = sum([(theta[F[j] + i]) for j in range(numTilings)])

            A = np.argmax(Q) if np.random.random() > epsilon \
                else np.random.randint(numActions)
            #I got to line ( A does not eqaul A star) line 13 
            break
        

        #end of our code
        print "Episode: ", episodeNum, "Steps:", step, "Return: ", G
        returnSum = returnSum + G
    print "Average return:", returnSum/numEpisodes
    runSum += returnSum
print "Overall performance: Average sum of return per run:", runSum/numRuns

#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()


