# collections.Counter()

from collections import Counter

X = int(input())
size = Counter(list(map(int, input().split())))
cust = int(input())
income = 0

for i in range(cust):
    shoe, price = map(int, input().split())
    if size[shoe]:
        income += price
        size[shoe] -= 1
print(income)

'''
Expected Output:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
200
'''
