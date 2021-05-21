num = 5
def sumofsq(num):
    list1 = []
    for i in range(1,num+1):
        list1.append(i**2)
    return sum(list1)
    

sumofsq(num)

'''
Expected Output:
55
'''
