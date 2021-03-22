#Count the number of players having height between mean and first standard deviation
#First calculate the Mean and Standard Deviation and put them in range

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
count = 0
for i in players:
    if i in range(179, 200):
        count += 1
print(count)
        
'''
Expected Output:
6
'''
