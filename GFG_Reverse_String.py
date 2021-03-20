#Reverse words in a string

def revstr(string):
  rev = string[::-1]
  for word in rev:
    print(word, end = "")

revstr("Hello My Name is Rahul")

'''
Expected Output:
luhaR si emaN yM olleH
'''
