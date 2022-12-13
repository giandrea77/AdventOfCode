#
# How to use: 
# $ python3 d3_p2.py < input_d3.txt 
#

total = 0


while True:
    try:
        x = input()
        y = input()
        z = input()
    except:
        break

    k, = set(x) & set(y) & set(z)

    if k >= "a":
        total += ord(k) - ord("a") + 1
    else:
        total += ord(k) - ord("A") + 27


print (total)