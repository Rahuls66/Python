# Program to find factorial of a number takena s input from user.

n = int(input())
inp = n
i = 1
factorial = 1

if n < 0:
    factorial = 0
elif n == 1 or n == 0:
    factorial = 1
else:
    while n > 0:
        factorial = factorial * n
        n -= 1
print(inp,"! is",factorial)

'''
Expected Output:
4 ! is 24
'''
