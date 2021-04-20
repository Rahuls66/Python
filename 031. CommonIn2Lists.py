# Python function that takes two lists and returns True if they have at least one common member.

def twoList(l1, l2):
  for i in l1:
    if i in l2:
      return True
      break

twoList([1,2,3,4], [4,5,6,7])

'''
Expected Output:
True
'''
