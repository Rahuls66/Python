num = 6
def sumofcube(num):
    list1 = []
    for i in range(1, num+1):
        list1.append(i**3)
    return sum(list1)

sumofcube(5)        

'''
Expected Output:
225
'''
