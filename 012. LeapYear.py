year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a Leap Year")
        else:
            print("It's not a Leap Year")
    else:
            print("It's a Leap Year")
else:
            print("It's not a Leap Year")
'''
Expected Output:
Test Case I:
Enter the year: 2020
It's a Leap Year

Test Case II:
Enter the year: 2013
It's not a Leap Year

Test Case III:
Enter the year: 1900
It's not a Leap Year
'''
