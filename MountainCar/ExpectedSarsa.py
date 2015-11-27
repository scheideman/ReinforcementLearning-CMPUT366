import blackjack
import numpy as np

numStates  = 180
numActions =   2
gamma = 1.0

numEpisodesLearn =  1000000
numEpisodesEval  = 10000000
alpha = 1e-3
eps_mu = 1e-2
eps_pi = 1e-2
Q = 1e-4 * np.random.random((2 + numStates, numActions))
Q[-1] = np.zeros((numActions))

returnSum = 0.0
for episodeNum in xrange(numEpisodesLearn):
    G = 0.0
    s = blackjack.init()
    while (s != -1):
        a = np.argmax(Q[s]) if np.random.random() > eps_mu \
            else np.random.randint(numActions)
        (r, sp) = blackjack.sample(s, a)
        v_pi = eps_pi * np.average(Q[sp]) + (1 - eps_pi) * np.max(Q[sp])
        Q[s, a] += alpha * (r + gamma * v_pi - Q[s, a])
        G = r + gamma * G
        s = sp
    returnSum += G
    ep = episodeNum + 1 
    if (ep % 10000 == 0):
        print "Episode: ", ep, "Average return: ", returnSum / ep
print "Average return while learning: ", returnSum / numEpisodesLearn

greedy = lambda s: np.argmax(Q[s])
blackjack.printPolicy(greedy)

returnSum = 0.0
for episodeNum in xrange(numEpisodesEval):
    G = 0.0
    s = blackjack.init()
    while (s != -1):
        (r, s) = blackjack.sample(s, greedy(s))
        G = r + gamma * G
    returnSum += G
print "Average return on deterministic policy: ", returnSum / numEpisodesEval
