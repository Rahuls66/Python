#Write a Python function descending(ls) that returns True if each element in its input list is at least as small as the one before it. For empty list, it should be True.
#Here are some examples to show how your function should work.
#descending([]) #returns True
#descending([4, 3, 3]) #returns True
#descending([7,18,17,19]) #returns False

def descending(ls):
    for i in range(len(ls)-1):
            if ls[i] >= ls[i+1]:
                continue
            else:
                return False
    return True

