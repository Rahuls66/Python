mi = 5
#Accept User Input:
#mi = float(input("Enter distance in Miles: "))

if mi >= 1:
    print("Entered Input for distance is: ", mi, "mi")
    km = mi * 1.60934
    print("Distance Value in Kilometers is:  ", round(km,2), "kms")
else:
    print("Please enter a valid input")
    pass

'''
Expected Output:

Entered Input for distance is:  5 mi
Distance Value in Kilometers is:   8.05 kms
'''
