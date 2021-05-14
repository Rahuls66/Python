# Nested Lists

n = int(input())
l1 = []
score1 = set()
second_lowest_name = []

for i in range(n):
    name = input()
    score = float(input())
    k = [name, score]
    l1.append(k)
    score1.add(score)
    
second_lowest_score = sorted(score1)[1]

for name, score in l1:
    if score == second_lowest_score:
        second_lowest_name.append(name)

for name in sorted(second_lowest_name):
    print(name, end = '\n')
    
'''
Expected Output:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Berry
Harry
'''
