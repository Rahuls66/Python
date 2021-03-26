'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer. 
Example: If the following tuples are given as input to the program: 
UP 5 DOWN 3 LEFT 3 RIGHT 2 
Then, the output of the program should be: 2
'''

import math
x = 0
y = 0

while True:
    steps = input()
    if steps == "":
        break
    else:
        steps = steps.split()
        if steps[0] == 'UP':
            y = y + int(steps[1])
        elif steps[0] == 'DOWN':
            y = y - int(steps[1])
        elif steps[0] == 'RIGHT':
            x = x + int(steps[1])
        elif steps[0] == 'LEFT':
            x = x - int(steps[1])
        else:
            print("Invalid Step")

result = x**2 + y**2
print(round(math.sqrt(result)))


'''
Expected Output:
UP 5
DOWN 3
LEFT 3
RIGHT 2

2
'''
