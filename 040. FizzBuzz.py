#Program which iterates the integers from 1 to 50. For multiple of 3, print Fizz.
#For multiple of 5, print Buzz, For multiple of 3 and 5, print FizzBuzz.

def FizzBuzz():
  for i in range(1,51):
    if i % 3 == 0:
      print("Fizz")
      continue
    elif i % 5 == 0:
      print("Buzz")
      continue
    elif (i % 3 == 0) and (i % 5 == 0):
      print("FizzBuzz")
      continue
    print(i)

FizzBuzz()

'''
Expected Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
Fizz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
Fizz
46
47
Fizz
49
Buzz
'''
