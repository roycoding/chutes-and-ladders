# chutesladdersmonte.py

# A Monte Carlo simulation of Chutes and Ladders.
# As described by Nick Berry at http://www.datagenetics.com/blog/november12011/index.html

import random
import pylab as pl
import numpy as np
import pickle

random.seed()

def dieroll():
    '''Return integer result of random die roll.'''
    return random.randint(1,6)

def move(board,location,chutes,ladders):
    '''Roll die once and move player accordingly.'''

    newloc = location + dieroll()

    if newloc >= board:
        location = board
    elif newloc in chutes:
        location = chutes[newloc]
    elif newloc in ladders:
        location = ladders[newloc]
    else:
        location = newloc

    return location

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

# Board size
board = 10*10
# Number of games to simulate
games = int(1e5) 
# Cutoff if game has not been won
maxmoves = 500

def monte():
    # Scoring array to tally number or of moves to win each game.
    data = np.zeros(maxmoves)

    for k in range(games):
        counter = 0
        location = 0
        while counter <= maxmoves and location < board:
            counter += 1
            location = move(board,location,chutes,ladders)
        data[counter] += 1


#dfile = open('monte-data.pkl','wb')
#pickle.dump(data,dfile)
#dfile.close()

#pl.plot(range(500),data)
#pl.show()
