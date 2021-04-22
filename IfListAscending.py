# Python function to check whether the list is in Ascending order or not

def Ascending(l1):
  tempList = l1[:]
  l1.sort()
  if tempList == l1:
    return True
  else:
    return False

Ascending([4,3,2,0])

'''
Expected Output:
False
'''
