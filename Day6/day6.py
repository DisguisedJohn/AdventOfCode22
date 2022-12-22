################## AdventOfCode day6 ################## 

####################################################### 
import os
os.system('clear')

def main():
    with open(os.path.dirname(__file__) + "/" +'input.txt') as f:  #Opens file and reads data to string "lines"
        lines = f.read()

    buffer = ""
    counter = -1 #I was one off so I overcorrected it here :3
    filling = True
    for letter in lines:
        counter += 1
        if filling == True:
            buffer += letter
            print(len(buffer))
            if len(buffer) >= 4:
                filling = False
        else:
            if buffer[0] == buffer[1] or buffer[0] == buffer[2] or buffer[0] == buffer[3] or buffer[1] == buffer[2] or buffer[1] == buffer[3] or buffer[2] == buffer[3]:
                print(buffer)
                buffer = buffer[1:] + letter
                print("Found repetition")
            else:
                print("END, {}, buffer: {}".format(counter, buffer))
                break


main()
