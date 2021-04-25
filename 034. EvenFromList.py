#Take inpur from users and Get the Even Numbers from the input numbers into a list

def evenNum(List):
    return([i for i in List if i % 2 == 0])

l1 = map(int, input().split())
evenNum(l1)

'''
Expected Output:
1 2 3 4 5 6 7
[2, 4, 6]
'''
