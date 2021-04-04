#HR
#Unique Elements

n = int(input())
l1 = []
for i in range(n):
  k = str(input())
  l1.append(k)

s1 = set(l1)
print(len(s1))

'''
Expected Output:
7
UK
China
USA
France
New Zealand
UK
France
5
'''
