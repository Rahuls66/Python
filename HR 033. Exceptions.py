# Exceptions

n = int(input())
t = []

for i in range(n):
    a, b = input().split()
    t.append([a,b])
for j in t:
    try:
        print(int(j[0])//int(j[-1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except Exception as e:
        print("Error Code:",e)
        
'''
Expected Output:
3
1 0
2 $
3 1
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''
 
