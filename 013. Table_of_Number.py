#Function to print Numeric Table for number returned from user

def table (num):
    for j in range(1,11):    
        print(str(num) + " X " + str(j) + " = " + str(num*j))
        j += 1

count = int(input("Enter the number for which you want table: \t"))
table(count)

"""
Expected Output:
Enter the number for which you want table:  4
4 X 1 = 4
4 X 2 = 8
4 X 3 = 12
4 X 4 = 16
4 X 5 = 20
4 X 6 = 24
4 X 7 = 28
4 X 8 = 32
4 X 9 = 36
4 X 10 = 40
"""
