#43. Check Subset

T = int(input())
for _ in range(T):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B)) 
    
'''
Expected Output:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
True
1
2
5
3 6 5 4 1
False
7
1 2 3 5 6 8 9
3
9 8 2
False
'''
