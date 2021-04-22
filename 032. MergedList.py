#Python function that takes two sorted lists and return merged List

def mergeList(l1, l2):
  l1.extend(l2)
  return l1

mergeList([1,2,3,4], [5,6,7,8])

'''
Expected Output:
[1, 2, 3, 4, 5, 6, 7, 8]
'''
