#45. Collections.deque()

from collections import deque

d = deque()
N = int(input())
for i in range(N):
    inp = input().split()
    if inp[0] == 'append':
        d.append(int(inp[1]))
    if inp[0] == 'appendleft':
        d.appendleft(int(inp[1]))
    if inp[0] == 'pop':
        d.pop()
    if inp[0] == 'popleft':
        d.popleft()

for i in d:
    print(i, end = " ")
    
'''
Expected Output:
6
append 1
append 2
append 3
appendleft 4
pop
popleft
1 2
'''
