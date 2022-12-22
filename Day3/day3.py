################## AdventOfCode day3 ################## 

####################################################### 
import os
os.system('cls')


with open(os.path.dirname(__file__) + "/" +'input.txt') as f:  #Opens file and reads data to string "lines"
    lines = f.readlines()
same_letters = list()
for line in lines:
    clean_line = line.replace("\n","")
    groups = [clean_line[:int((len(clean_line)/2))], clean_line[int(len(clean_line)/2):]]
    # print("{first}, {second}".format(first = len(groups[0]), second=len(groups[1])))
    # print("{first}, {second}".format(first = groups[0], second=groups[1]))
    for letter_A in groups[0]:
        same_letter = ""
        for letter_B in groups[1]:
            if letter_A == letter_B:
                same_letter = letter_A
                break
        if same_letter != "":
            break
    if same_letter != "":
        same_letters.append(same_letter)
sum = 0
for letter in same_letters:
    if ord(letter) >= 97:
        sum += (ord(letter)-96)
    else:
        sum += (ord(letter)-38)
print(sum)