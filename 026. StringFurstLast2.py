# Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return empty string.

def frls(s):
  if len(s) > 2:
    return (s[:2]+s[-2:])
  else:
    return ""

frls("Abracadabra")

'''
Expected Output:
'Abra'
'''
