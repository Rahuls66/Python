#Check for the passwords and return the legit password from the given passwords - ABd1234@1,a F1#,2w3E*,2We3345

import re
passw = input().split(",")
#print(passw)
list1 = []

for word in passw:
  if not re.search('[a-z]', word):
    continue
  elif not re.search('[0-9]', word):
    continue
  elif not re.search('[A-Z]', word):
    continue
  elif not re.search('[$#@]', word):
    continue
  elif (len(word) < 6 or len(word) > 12):
    continue
  else:
    list1.append(word)
for i in list1:
  print(i)
  
'''
Expected Output:
ABd1234@1,a F1#,2w3E*,2We3345
ABd1234@1
'''
