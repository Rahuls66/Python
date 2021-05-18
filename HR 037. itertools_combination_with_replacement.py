# itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

S, k = input().split()
S = sorted(S.upper())
k = int(k)
comb = list(combinations_with_replacement(S, k))
for i in comb:
    print("".join(i))
    
'''
Expected Output:
HACK 2
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
