m = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

print (f'player 1 sees {m[0:7]}')
print (f'player 2 sees: {m[7:14]}')

def p1_turn():
    p = input('player 1: pick a pit (1-6): ')
    p = int(p) - 1                                  # convert string to int and subtract 1 for index
    if m[p] == 0 or p == '':                        # i pressed enter without selection and crashed it
        print ('pick another pit')                  # error
        p1_turn()                                   # recursion, can omit if we assume player 1 always picks a valid pit
    else:
        seeds = m[p]                                # seeds in pit p
        for i in range(p + 1, p + m[p] + 2):        # add 1 to pit index to get index of next stone
            m[i % 14] += 1                          # mod 14 to wrap around, this is super clever
        m[p] = 0
        # rule for if the last stone ends in your mancala, you get an extra turn
        if (p + seeds) % 14 == 7:    
            p1_turn()

        # rule for if the last stone lands in an empty pit, you get the seeds from the opposite pit
            # need to make sure this doesn't go out of range of the index somehow
            # unsure how to do this
            # sometimes it crashes when the p + seeds > the length of the list, but sometimes it does not.
            # error is in the mancala, does not happen for other pits?

            m[7] = m[7] + m[(p + seeds) % 14] + m[(p + seeds + 7) % 14] # add to mancala
            m[(p + seeds) % 14] = 0                                     # empty the pit
            m[(p + seeds + 7) % 14] = 0                                 # empty the opposite pit  



        print (f'player 1 sees: {m[0:7]}')
        print (f'player 2 sees: {m[7:14]}')
        if m[0:7].count(0) == 6 or m[7:14].count(0) == 6:
            print ('game over')
            print ('player 1 wins') if m[7] > m[14] else print ('player 2 wins')
        else:
            p2_turn()

def p2_turn():
    p = input('player 2: pick a pit (1-6): ')
    p = int(p) - 1
    if m[p] == 0 or p == '':
        print ('pick another pit')
        p2_turn()
    else:
        seeds = m[p]
        for i in range(p + 1, p + m[p] + 2):
            m[i % 14] += 1
        m[p] = 0

        if (p + seeds) % 14 == 14:
            p2_turn()
            
        if m[(p + seeds) % 14] == 1:
            m[14] = m[14] + m[(p + seeds) % 14] + m[(p + seeds + 7) % 14]
            m[(p + seeds) % 14] = 0
            m[(p + seeds + 7) % 14] = 0


        print (f'player 1 sees: {m[0:7]}')
        print (f'player 2 sees: {m[7:14]}')
        if m[0:7].count(0) == 6 or m[7:14].count(0) == 6:
            print ('game over')
            print ('player 1 wins') if m[7] > m[14] else print ('player 2 wins')
        else:
            p1_turn()

# start the game
p1_turn()