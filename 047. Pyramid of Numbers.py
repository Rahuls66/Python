#Square Pyramid

T = int(input())
for _ in range(T):
    num = int(input())
    for i in range(1,num+1):
        for j in range(1, num+1-i):
            print(' ', end='')
    
        for j in range(1,i+1):
            print(j, end='')
    
        for j in range(i-1,0,-1):
            print(j, end='')
    
        print()
    print(end = '\n')
