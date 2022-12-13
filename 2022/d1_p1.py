#
# Advent of code: Day1 part 1
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
    
max_value = max(calories.values())  # maximum value
print(max_value)