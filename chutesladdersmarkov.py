# chutesladdersmarkov.py

# A Markov chain simulation of Chutes and Ladders.
# As described by Nick Berry at http://www.datagenetics.com/blog/november12011/index.html

import pylab as pl
import numpy as np
import json

# Location of chutes and ladders
# start space : end space
chutes = {
    98:78,
    95:75,
    93:73,
    87:24,
    64:60,
    62:19,
    56:53,
    49:11,
    48:26,
    16:6}

ladders = {
    1:38,
    4:14,
    9:31,
    21:42,
    28:84,
    36:44,
    51:67,
    71:91,
    80:100}

# Transition matrix. 101 x 101, to in starting position off board.
boardsize = 10*10 + 1

# Probability to roll an arbitrary number with single die.
p = 1./6

# Generate generic transition matrix, then modify
T = []

for k in range(boardsize):
    T += [(k+1)*[0.]+[p,p,p,p,p,p]+(boardsize-7-k)*[0.]]

# Modify last element to account for landing on last square (winning)
for k in range(6):
    if k < 5:
        T[k-6][-2-k:] = [(2+k)*p]
    else:
        # Last row handled differently
        T[k-6][-2-k:] = [1.0]

# Modify transition matrix based on presence of chutes and ladders
def addobstacles(obstacles):
    for j in obstacles:
        # Modify row with obstacle and proceeding 5 rows (if on board)
        for k in [x for x in (j - np.arange(6)) if x >= 0]:
            T[k][j] = T[k][j] - p
            T[k][obstacles[j]] = T[k][obstacles[j]] + p

addobstacles(chutes)
addobstacles(ladders)

T = np.array(T)

# Vector of game piece location probabilities (101 spaces)
L = np.zeros(10*10+1)
# Intial position. Probability = 1.0
L[0] = 1.0

# Moves to simulate
moves = 50
# Probability of landing in square 100+
gamefinish = []
# Save boards (L) for each subsequent move
boards = []

# Propagate game piece via Markov process!
for k in range(moves):
    L = np.dot(L,T)
    boards += [L.tolist()]
    gamefinish += [L[100]]

# Calculate differential winning probability distribution from cummulative distribution
diff = []
for k in range(len(gamefinish)-1):
    diff += [gamefinish[k+1] - gamefinish[k]]

# Export boards to JSON file for further analysis
json.dump(boards,open('markovboards.json','w'))

# Plotting
# Display board with probability of being on a given square
#board = pl.matshow(L[1:].reshape(10,10),cmap='Reds', origin='lower')
#board.get_axes().axis('off')

# Plot differential winning probability of each move
#pl.plot(gamefinish)
#pl.plot(diff)

#pl.show()
