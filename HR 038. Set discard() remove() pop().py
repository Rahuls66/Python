# Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
l = int(input())
for i in range(l):
    z = input().split()
    if z[0] == 'pop':
        s.pop()
    elif z[0] == 'discard':
        s.discard(int(z[1]))
    else:
        s.remove(int(z[1]))
print(sum(s))

'''
Expected Output:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
4
'''
