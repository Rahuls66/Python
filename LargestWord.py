#To Print the word with largest length from the input string
txt = input()
k = txt.split(' ')
l1 = []

for text in k:
    length = len(text)
    l1.append(length)
print(l1)
index = l1.index(max(l1))
print(k[index])
