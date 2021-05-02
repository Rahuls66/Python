# Take 5 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

def copy(l1):
  l2 = []
  l2 = l1.copy()
  return l2[::-1]

l1 = list(map(int, input().split()))
copy(l1)

#Using for loop
'''
l1= []
for i in range(5):
  l1.append(int(input()))

l2 = l1[::-1]
print(l2)
'''

#Using For Loop, copy() and revrse()
'''
l1= []
for i in range(5):
  l1.append(int(input()))

l2 = l1.copy()
l2.reverse()
print(l2)
'''

'''
Expected Output:
1 2 3 4
[4, 3, 2, 1]
'''
