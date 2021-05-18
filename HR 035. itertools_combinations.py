# itertools.combinations()

from itertools import combinations

S, k = input().split()
S = sorted(S.upper())
k = int(k)
for z in range(1, k+1):
    comb = list(combinations(S, z))
    for i in comb:
        print("".join(i))
        
'''
Expected Output:
HACK 2
A
C
H
K
AC
AH
AK
CH
CK
HK
'''
