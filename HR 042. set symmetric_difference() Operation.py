# Set .symmetric_difference() Operation

n = int(input())
m = map(int, input().split())
m = set(m)
b = int(input())
l = map(int, input().split())
l = set(l)
print(len(m.union(l) - m.intersection(l)))

'''
Expected Output:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
8
'''
