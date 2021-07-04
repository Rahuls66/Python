# Compress the String!

from itertools import groupby

for i, n in groupby(input()):
        a = list(n)  
        print("(", len(a), ", ", i, ")", end = " ", sep = "")
        
'''
Expected Output:
1222311
(1, 1) (3, 2) (1, 3) (2, 1)
'''
