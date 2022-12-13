from collections import Counter

total = 0

with open('input_d3.txt') as file_input:

    for line in file_input:
        
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        
        # Create a merge tuple with the merge of two subsets 
        k, = set(firstpart) & set(secondpart)
        if k >= "a":
            total += ord(k) - ord("a") + 1
        else:
            total += ord(k) - ord("A") + 27

print (total)

