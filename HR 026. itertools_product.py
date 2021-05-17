# itertools.product()

from itertools import product
a = input().split()
a = list(map(int, a))
b = input().split()
b = list(map(int, b))

a = list(product(a,b))
for i in a:
    print(i, end = " ")

'''
Expected Output:
1 2
3 4
(1, 3) (1, 4) (2, 3) (2, 4) 
'''
