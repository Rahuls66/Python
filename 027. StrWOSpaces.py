# Consider a string s= “Hello how are you?”. Write a program to return this string without spaces.

def withoutSp(s):
  #return "".join(s.split())
  return s.replace(" ", "")

withoutSp("Hello how are you?")

'''
Expected Output:
Hellohowareyou?
'''
