################## AdventOfCode day2 ################## 
# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z

# This strategy guide predicts and recommends the following:

#     In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#     In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#     The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?
####################################################### 

def get_points(oponent, us):
    points={"draw": 3, "lose":0, "win":6, "X":1, "Y":2, "Z":3}


    if oponent == 'A': #Rock
        if us == 'X': #Rock
            #draw
            sum = points['draw'] + points['X']
        elif us == 'Y': #Paper
            #lose
            sum = points['win'] + points['Y']
        elif us == 'Z': #Scissors
            #win
            sum = points['lose'] + points['Z']

    elif oponent == 'B': #Paper
        if us == 'X': #Rock
            #win
            sum = points['lose'] + points['X']
        elif us == 'Y': #Paper
            #draw
             sum = points['draw'] + points['Y']
        elif us == 'Z': #Scissors
            #lose
            sum = points['win'] + points['Z']

    elif oponent == 'C': #Scissors
        if us == 'X': #Rock
            #lose
            sum = points['win'] + points['X']
        elif us == 'Y': #Paper
            #win
            sum = points['lose'] + points['Y']
        elif us == 'Z': #Scissors
            #draw
            sum = points['draw'] + points['Z']
    return sum



with open('input.txt') as f:  #Opens file and reads data to string "lines"
    lines = f.readlines()

total_sum = 0
for match in lines:
    total_sum += get_points(match[0], match[2])
print(total_sum)

