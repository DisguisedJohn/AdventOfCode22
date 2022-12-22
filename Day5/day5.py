################## AdventOfCode day3 ################## 

####################################################### 
import os
os.system('cls')
pile = [list(),list(),list(),list(),list(),list(),list(),list(),list(),list()]
pile[0] = list()
pile[1] = ['B','L','D','T','W','C','F','M']
pile[2] = ['N','B','L']
pile[3] = ['J','C','H','T','L','V']
pile[4] = ['S','P','J','W']
pile[5] = ['Z','S','C','F','T','L','R']
pile[6] = ['W','D','G','B','H','N','Z']
pile[7] = ['F','M','S','P','V','G','C','N']
pile[8] = ['W','Q','R','J','F','V','C','Z']
pile[9] = ['R','P','M','L','H']

def move_boxes(number, from_pile, to_pile):
    for i in range(int(number)):
        box = pile[int(from_pile)].pop(-1)
        pile[int(to_pile)].append(box)
    pass

def print_top_boxes():
    print("{}{}{}{}{}{}{}{}{}".format(pile[1][-1], pile[2][-1], pile[3][-1], pile[4][-1], pile[5][-1], pile[6][-1], pile[7][-1], pile[8][-1], pile[9][-1]))

def main():
    print_top_boxes()
    with open(os.path.dirname(__file__) + "/" +'input.txt') as f:  #Opens file and reads data to string "lines"
        lines = f.readlines()
    commands = lines[10:]
    for command in commands:
        stripped_command = command.replace("\n","")
        stripped_command = stripped_command.replace("move","")
        stripped_command = stripped_command.replace("from",";")
        stripped_command = stripped_command.replace("to",";")
        stripped_command = stripped_command.replace(" ","")

        separated_command = stripped_command.split(";")
        move_boxes(separated_command[0], separated_command[1], separated_command[2])
    print_top_boxes()


main()