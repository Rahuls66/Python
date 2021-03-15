x = 8
y = 10

#To accept inptu from user:
#x = float(input("Enter x value: "))
#y = float(input("Enter y value: "))

print("Old x Value is: ", x)
print("Old y Value is: ", y)

k = x  # Assigning x value to a new variable k
x = y  # Assigning y value to 
y = k  # Assigning k variable value to y

#Another Method:
#x, y = y, x

print("\n")
print("New x Value is: ", x)
print("New y Value is: ", y)

'''
Expected Output:

Old x Value is:  8
Old y Value is:  10


New x Value is:  10
New y Value is:  8
'''
