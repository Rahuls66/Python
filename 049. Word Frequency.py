import collections
def WordCount(s):
    k = collections.Counter(s.split())
    dic = {}
    for key, value in k.items():
        dic[key] = value
    print(dic)
  
#read a string S
S = input()

#Call the function
WordCount(S)
