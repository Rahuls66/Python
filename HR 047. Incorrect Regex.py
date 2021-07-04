#Incorrect Regex

import re

T = int(input())
for _ in range(T):
    s = input()
    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)
               
'''
Expected Output:
2
.*\+
True
.*+
False
'''
