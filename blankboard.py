# blankboard.py

# This is a quick hack to generate the array code for a Chutes and Ladders transition matrix
#   for the Markov chain program. The board has no chutes or ladders. Manually copy and paste
#   the output and edit the chutes and ladders. A hack and a half.

# Board size (plus one for starting position)
board = 10*10 + 1

# Probability to roll an arbitrary number with a single die.
p = 1./6

for k in range(board):
    print (k+1)*[0]+[p,p,p,p,p,p]+(board-7-k)*[0],','
