# Finding the percentage

n = input()
students = {}
for i in range(int(n)):
  a = input().split()
  name = a[0]
  marks = a[1:]
  marks = list(map(float, marks))
  students[name] = marks
req_name = input()
req_marks = students[req_name]

print(sum(req_marks) / len(req_marks))

'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
56.00
'''
