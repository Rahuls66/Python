# Collections.namedtuple()

from collections import namedtuple

N = int(input())
f = input()
total = 0
Students = namedtuple('Students', f)

for i in range(N):
    head = input().split()
    marks = Students(*head)
    total += int(marks.MARKS)

print('{0:2f}'.format(total / N))


'''
Expected Output:
    5

    ID         MARKS      NAME       CLASS

    1          97         Raymond    7

    2          50         Steven     4

    3          91         Adrian     9

    4          72         Stewart    5

    5          80         Peter      6
    
78.00
'''
