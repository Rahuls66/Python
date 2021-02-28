#num = 5

#Accept User Input:
num = int(input("Enter Number: "))

if num > 1:   
    for i in range(2, num):
        if num % i == 0:     
            print("It's not a Prime Number")
            break         
    else:
        print("It's a Prime Number") 
else:                                 
    print("It's Not a Prime Number")   

'''
Expected Output:

Enter Number: 44
It's not a Prime Number

Enter Number: 23
It's a Prime Number
'''
