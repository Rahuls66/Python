# Alphabet Rangoli

def print_rangoli(size):
    s = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = s[size:x:-1]+s[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)

print_rangoli(5)

'''
Expected Output:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
