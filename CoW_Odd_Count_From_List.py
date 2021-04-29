'''
Problem from COde of Wars
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''

def find_it(x):
    l1 = []
    for i in x:
        if x.count(i) % 2 != 0:
            if i not in l1:
                l1.append(i)
    return (l1) 

    find_it([1,2,3,4,5,1,3,3,4])

'''
Expected Output:
[2, 3, 5]
'''
