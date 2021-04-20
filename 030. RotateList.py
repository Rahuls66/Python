# A list rotation consists of taking the last element and moving it to the front. For instance, if we rotate the list [1,2,3,4,5], we get [5,1,2,3,4]. 
# If we rotate it again, we get [4,5,1,2,3]. Write a Python function rotatelist(ls,k) that takes a list ls and a positive integer k and returns 
# the list ls after k rotations. If k is not positive, your function should return ls unchanged. Note that your function should not change ls itself,
# and should return the rotated list.

def rotateList(ls, k):
  if int(k) > 0:
    for i in range(int(k)):
      ls.insert(0, ls[-1])
      ls.pop()
    return ls
  else:
    return ls 

rotateList([1,2,3,4,5], 12)

'''
Expected Output:
[4, 5, 1, 2, 3]
'''
