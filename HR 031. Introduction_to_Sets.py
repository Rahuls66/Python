# Introduction to Sets

def average(array):
    avg = sum(set(array)) / len(set(array))
    return avg  

n = int(input())
arr = list(map(int, input().split()))
average(arr)

'''
10
161 182 161 154 176 170 167 171 170 174
169.375
'''
