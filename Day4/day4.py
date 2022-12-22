################## AdventOfCode day3 ################## 

####################################################### 
import os
os.system('cls')

def interval_to_range(interval):
    start, stop = interval.split("-")
    return int(start), int(stop)

def main():
    with open(os.path.dirname(__file__) + "/" +'input.txt') as f:  #Opens file and reads data to string "lines"
        lines = f.readlines()

    overlap_counter = 0
    line_counter = 1
    for line in lines:
        line = line.replace("\n","")
        elf1, elf2 = line.split(",")

        elf1_start, elf1_stop = interval_to_range(elf1)
        elf2_start, elf2_stop = interval_to_range(elf2)
        
        if (elf1_start <= elf2_start and elf1_stop >= elf2_stop) or (elf2_start <= elf1_start and elf2_stop >= elf1_stop):
            overlap_counter += 1
    print(overlap_counter)
main()
#interval_to_list("12-12")

