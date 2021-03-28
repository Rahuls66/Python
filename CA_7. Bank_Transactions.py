#Calculate the Net effcetive Balance after a seried of Bank Transactions 
#Where D refers to Deposit and W refers to Witdrawl

total = 0
while True:
  transc = input()
  if transc == "":
    break
  else:
    transc = transc.split(" ")
    if transc[0] == 'W':
      total = total - int(transc[1]) 
    elif transc[0] == 'D':
      total = total + int(transc[1])
    else:
      print("Invalid transaction type")
print(total)

'''
Expected Output:
W 500
D 200
W 200

-500
'''
