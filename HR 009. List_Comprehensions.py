# List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lis1 = [[num,num1,num2] for num in range(0,x+1) for num1 in range(0,y+1) for num2 in range(0,z+1) if num + num1 + num2 != n]
print(lis1)

'''
Expected output:
1
1
1
2
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
