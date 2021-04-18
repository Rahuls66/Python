# Program to identify palindrome words in a line of text

def isPalindrome(s):
  k = s.split()
  for i in k:
    if len(i) > 1:
      if i[:] == i[::-1]:
        print(i, "is Palindrome")

isPalindrome(Hello I am madam and I speak malayalam)

'''
Expected Output:
madam is Palindrome
malayalam is Palindrome
'''
