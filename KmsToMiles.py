km = 5
#Accept User Input:
#km = float(input("Enter distance in Kilometers: "))

if km > 1:
    print("Entered Input for distance is: ", km, "kms")
    miles = km / 1.60934
    print("Distance Value in Miles is:  ", round(miles,2), "mi")
elif km == 1:
    print("Entered Input for distance is: ", km, "km")
    miles = km / 1.60934
    print("Distance Value in Miles is:  ", round(miles,2), "mi")
else:
    print("Please enter a valid input")
    pass
'''
Expected Output:
Entered Input for distance is:  5 kms
Distance Value in Miles is:   3.11 mi
'''
