#44. DefaultDict Tutorial

from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())
for i in range(n):
    d[input()].append(str(i+1))
a = [input() for i in range(m)]

for i in a:
    if i in d:
        print(" ".join(map(str, d[i])))
    else:
        print(-1)
 
'''
Expected Output:
5 2
a
a
b
a
b
a
b
1 2 4
3 5
'''
