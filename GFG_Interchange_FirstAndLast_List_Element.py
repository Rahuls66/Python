def myList(x):
    x[0], x[-1] = x[-1], x[0]
    return x

myList([1,2,3,4,5,6])

'''
Expected Output:
[6, 2, 3, 4, 5, 1]
'''
