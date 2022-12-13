#
# Advent of code: Day1 part 2
#

calories = {0:0}
index = 0

with open('input.txt') as file_input:

    for line in file_input:
        
        if line.isspace():
            index += 1
            calories[index] = 0            
        else:
            calories[index] = calories[index] +  int(line)

calories_array = list(calories.values())
calories_array = sorted(calories_array, reverse=True)

print (sum(calories_array[0:3]))