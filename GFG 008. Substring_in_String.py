#Check if given substring is present in given string

def substr(string, substring):
  if string.find(substring) >= 0:
    print('Substring', substring, "is present in the string", string)

substr('Hello My name is Rahul', 'Rahul')

'''
Expected Output:
Substring Rahul is present in the string Hello My name is Rahul
'''
