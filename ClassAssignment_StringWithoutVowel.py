#Write a function that takes a string and return new strings with all vowel removed

import re

def troller(string):
    new_str = re.findall("[^aeiouAEIOU]+", string)
    for txt in (new_str):
        print(txt, end = "")

troller("This website is for losers LOL!")

'''
Expected Output:
Ths wbst s fr lsrs LL!
'''
