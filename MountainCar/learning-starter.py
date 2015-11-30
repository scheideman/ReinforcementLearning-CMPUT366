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
	    #print("while")
            tilecode(position,velocity,F)
	    #print("pos",position,"\n","velocity", velocity)    
	    #print("F",F)
            for a in range(3):
                i = a*4*9*9
                Q[a] = sum([(theta[j+i]) for j in F])

 	    if np.random.random() > epsilon:
		A = np.argmax(Q)
            else:
		 np.random.randint(numActions)
            print("A",A)
            R,result = mountaincar.sample((position,velocity),A)
            if (result == None):
		print("terminal")
                #I don't know what to put here, what is the theta index of terminal state
		exit()
                break
            newPosition=result[0]
            newVelocity=result[1]

	    tilecode(newPosition,newVelocity,F) 
  	   
            error = R - Q[A]
		
	  
            
            for j in F:
                e[j+(A*4*9*9)] = 1
            
            for a in range(3):
                i = a*4*9*9
                Q[a] = sum([(theta[j+i]) for j in F])
                
            #expectedValue = sum([(theta[j+A]) for j in F]) 			

            error = error + (1-epsilon)*(np.argmax(Q)) + epsilon*(np.average(Q))

	    for j in range(n):
		theta[j] = theta[j] + alpha*error*e[j]

	    for j in range(n):
		value=0
		if j in F:
			value=1
		if j-(4*9*9) in F:
			value=1
		if j-(2*4*9*9) in F:
			value=1
	    	e[j] = max(lmbda*e[j],value) 	

            #for j in range(n):
             #   e[j]=gamma*lmbda*e[j] #comparing to feature vector?
          #      #e[j]=np.max(gamma*lmbda*e[j], ????) #comparing to feature vector?
            position, velocity = newPosition, newVelocity
        

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


