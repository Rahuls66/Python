# String Split and Join

def split_and_join(line):
    a = line.split(" ")
    return ('-'.join(a))
    
split_and_join('this is a string')

'''
Expected Output:
this-is-a-string
'''
