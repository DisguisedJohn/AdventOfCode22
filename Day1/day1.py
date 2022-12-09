################## AdventOfCode day1 ################## 
# 1000
# 2000
# 3000

# 4000

# 5000
# 6000

# 7000
# 8000
# 9000

# 10000

# This list represents the Calories of the food carried by five Elves:

#     The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
#     The second Elf is carrying one food item with 4000 Calories.
#     The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
#     The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
#     The fifth Elf is carrying one food item with 10000 Calories.

# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
####################################################### 
import os

with open(os.path.dirname(__file__) + "/" +'input.txt') as f:  #Opens file and reads data to string "lines"
    lines = f.read()

elfs_raw = lines.split('\n\n') #Splits string by "\n\n"
elfs = list() #New list of separated values

for elf in elfs_raw: #Go through list and separate string values
    elfs.append(elf.split('\n'))

elfs_sums = list() #List of sums
for elf in elfs:
    sum = 0
    for entry in elf:
        sum += int(float(entry))
    elfs_sums.append(sum)

print(max(elfs_sums))

#! Saved one for iteration 
# with open('input.txt') as f:  #Opens file and reads data to string "lines"
#     lines = f.read()

# elfs_raw = lines.split('\n\n') #Splits string by "\n\n"
# elfs = list() #New list of separated values

# max = 0
# for elf in elfs_raw: #Go through list and separate string values
#     elf_splitted = elf.split('\n')
#     sum = 0
#     for tiny_elf in elf_splitted:
#         sum += int(float(tiny_elf))
#     if max < sum:
#         max = sum
# print(max)

