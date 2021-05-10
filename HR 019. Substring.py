#Substring

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

count_substring('ABCDCDC', 'CDC')

'''
Expected Output:
2
'''
