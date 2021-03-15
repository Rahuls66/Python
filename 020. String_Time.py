"""
This program gives the ideal time required to type the input string
Time to type each letter is based on my typing speed
All time units in seconds
"""

alphabet = {"a":0.13, "b":0.14, "c":0.14, "d":0.15, \
"e":0.14, "f":0.15, "g":0.13, "h":0.13, "i":0.14, "j":0.14, \
"k":0.14, "l":0.13, "m":0.15, "n":0.12, "o":0.15, "p":0.13, \
"q":0.14, "r":0.13, "s":0.12, "t":0.14, "u":0.13, "v":0.15, \
"w":0.17, "x":0.15,"y":0.15, "z":0.13, " ":0.10}

def time(word):
    i = 0
    sum = 0
    for i in range(len(word)):
        k = word[i]
        sum += alphabet[k]
        i += 1
    print("The ideal time to write this word is",round(sum,2),"seconds!")

time("i love cycling")

"""
Expected Output:
The ideal time to write this word is 1.86 seconds!
"""
