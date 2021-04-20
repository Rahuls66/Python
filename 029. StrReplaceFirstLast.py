# Python program to change a given string to a new string where the first and last chars have been exchanged.

def flChange(s):
  f = s[0]
  l = s[-1]
  return l + s[1:-1] + f

flChange("Hello")

'''
Expected Output:
oellH
'''
