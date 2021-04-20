#Python program to remove the characters which have odd index values of a given string.

def remOdd(ste):
  newStr = ""
  for i in range(len(ste)):
    if i % 2 == 0:
      newStr = newStr + ste[i]
  return newStr

remOdd("Hello All")

'''
Expected Output:
HloAl
'''
