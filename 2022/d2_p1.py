# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

total = 0

with open('input_d2.txt') as file_input:

    for line in file_input:

        x, y = line.split()
        a = ord(x) - 65
        b = ord(y) - ord("X")

        total += b + 1

        if a == b:
            total += 3
        elif (b - a) % 3 == 1:
            total += 6

print(total)