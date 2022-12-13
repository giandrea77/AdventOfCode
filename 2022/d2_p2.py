# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

total = 0

with open('input_d2.txt') as file_input:

    for line in file_input:

        x, y = line.split()
        x = ord(x) - 65
        
        if y == "X":
            total += (x - 1) %3 + 1
        elif y == "Y":
            total += 3 + x + 1
        else:
            total += 6 + ( x + 1 ) % 3 + 1


print(total)