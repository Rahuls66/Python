#x = 7

#Accept User Input
x = int(input("Enter Number for which factorial to be calculated: "))
factorial = 1

for num in range(1 , x + 1):
    factorial = factorial * num

print(x,"! is: ", factorial) 

'''
Expected Output:
Enter Number for which factorial is tobe calculated: 4
4 ! is:  24
24
'''
