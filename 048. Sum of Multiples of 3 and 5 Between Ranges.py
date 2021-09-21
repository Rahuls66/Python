def SumOfMultiples(n):
  #your code here
  sum = 0
  for i in range(n+1):
    if (i % 3 == 0 or i % 5 == 0):
        sum = sum + i
    #return the value of sum
  print(sum)  
  
  
  
  
#Read the value of limit
n = int(input())
#call the function
SumOfMultiples(n)
