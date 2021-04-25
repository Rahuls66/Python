#Program to find the frequency of each letter in the given string (using Dictionary)

def Frequency(l1):
  d = {}
  for i in l1:
    if i in d.keys():
      d[i] += 1
    else:
      d[i] = 1
  return d

Frequency('abracadabra')
