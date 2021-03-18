#Program to find the minimum and maximumvalue from 10x10 matrix

arr2 = np.random.randint(1, 150, 100)
arr2 = arr2.reshape(10,10)
print("Maximum of Array: ", arr2.max())
print("Minimum of Array: ", arr2.min())

'''
Expected Output (may change based on random integers):
Maximum of Array:  148
Minimum of Array:  2
'''
