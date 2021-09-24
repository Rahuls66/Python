def SumOfDigits(n):
  sum = 0
  for i in str(n):
    sum = sum + int(i)
  print(sum)
  

#call the function here
SumOfDigits(int(input()))
