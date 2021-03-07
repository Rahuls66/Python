def fib(num):
    if num < 0:
        print("Invalid")
    elif num == 0 or num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)
        
fib(10)

'''
Expected Output:
34
'''
