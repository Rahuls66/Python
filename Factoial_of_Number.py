#Accept User Input
x = int(input("Enter Number for which factorial to be calculated: "))
factorial = 1

if x < 0:
    factorial = 0
elif x == 0 and x == 1:
    factorial = 1
else:
    for num in range(1 , x + 1):
        factorial = factorial * num

print(x,"! is: ", factorial) 

'''
Expected Output:
Enter Number for which factorial is tobe calculated: 4
4 ! is:  24

Enter Number for which factorial is tobe calculated: 0
0 ! is:  1

Enter Number for which factorial is tobe calculated: -1
0 ! is:  0
'''
