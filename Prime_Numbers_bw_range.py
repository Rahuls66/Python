urange = 100
lrange = 10
l1 = []

for i in range(lrange, urange + 1):
    if i > 1:
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            l1.append(i)
print(l1)

'''
Expected Output:
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''
