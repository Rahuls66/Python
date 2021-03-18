#Find Frequency of each element in the array

arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])

import collections
k = collections.Counter(arr)
for key, value in k.items():
    print(key, ":", value)
    
'''
Expected Output:
0 : 4
5 : 2
4 : 3
3 : 1
2 : 1
1 : 2
9 : 1
'''
