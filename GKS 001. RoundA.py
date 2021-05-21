T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    S = input()
    L = 0
    for j in range(N//2):
        if S[j] != S[N - j - 1]:
            L += 1
    print(f'Case #{i+1}: {K-L}')
    
'''
Expected Output:
2
5 1
ABCAA
Case #1: 0
4 2
ABAA
Case #2: 1
'''
