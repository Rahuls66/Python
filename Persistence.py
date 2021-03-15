#Write a fucntion persistence that takes in a  positive parameter num and returns its multiplicative persistence
#which is the number of times you must multiply the digits in num until you reach a single digit

def persistence(num):    
    count = 0
    while num > 9:
        num =  reduce(lambda x,y:x*y, [int(i) for i in str(num)])
        count += 1
    return count

num = int(input())
print(persistence(num))

'''
Expeced Output:
999
4
'''
