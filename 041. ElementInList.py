# Take 10 integer inputs from user and store them in a list. 
# Again ask user to give a number. Now, tell user whether that number is present in list or not.
# Iterate over list using while loop

def IsIn(l1, a):
  if a in l1:
    return True

l1 = list(map(int, input().split()))
a = int(input())
IsIn(l1, a)

'''
Expected Output:
1 2 3 4 5 6 7 8 9
3
True
'''
