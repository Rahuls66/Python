# Any or All

N = int(input())
inp = input().split()

if all(int(i) >= 0 for i in inp):
    if any(i == i[::-1] for i in inp):
        print("True")
    else:
        print("False")
else:
    print("False")
    
'''
Expected Output:
5
12 9 61 5 14
True
'''
