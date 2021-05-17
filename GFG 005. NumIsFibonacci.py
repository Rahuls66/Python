def perfsq(x):
    temp = int(x ** 0.5)
    if temp*temp == x:
        return True

def isFib(n):
    if perfsq(5*(n*n) + 4) or perfsq(5*(n*n) - 4) == True:
        return True
    
for i in range(1,20):
    if isFib(i) == True:
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is not a Fibonacci Number")
        
'''
Expected Output:
1 is a Fibonacci Number
2 is a Fibonacci Number
3 is a Fibonacci Number
4 is not a Fibonacci Number
5 is a Fibonacci Number
6 is not a Fibonacci Number
7 is not a Fibonacci Number
8 is a Fibonacci Number
9 is not a Fibonacci Number
10 is not a Fibonacci Number
11 is not a Fibonacci Number
12 is not a Fibonacci Number
13 is a Fibonacci Number
14 is not a Fibonacci Number
15 is not a Fibonacci Number
16 is not a Fibonacci Number
17 is not a Fibonacci Number
18 is not a Fibonacci Number
19 is not a Fibonacci Number
'''
