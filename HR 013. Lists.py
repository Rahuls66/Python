# Lists

num = int(input().strip())

l = []
for i in range(num):
    func = input().strip().split(" ")
    if func[0] == "append":
        l.append(int(func[1]))
    elif func[0] == "insert":
        l.insert(int(func[1]), int(func[2]))
    elif func[0] == "remove":
        l.remove(int(func[1]))
    elif func[0] == "pop":
        l.pop()
    elif func[0] == "sort":
        l.sort()
    elif func[0] == "reverse":
        l.reverse()
    elif func[0] == "print":
        print(l)
   
'''
Expected Output:
12
insert 0 5
insert 1 10
insert 0 6
print
[6, 5, 10]
remove 6
append 9
append 1
sort
print
[1, 5, 9, 10]
pop
reverse
print
[9, 5, 1]
'''
