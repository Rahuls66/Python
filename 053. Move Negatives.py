a = int(input())
l1 = []
for _ in range(a):
    l1.append(int(input()))
print(sorted(l1, key=lambda x: -x))
