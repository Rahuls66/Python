def balanced(expression):
    stack = []
    
    for c in expression:
        if(c == '('):
            stack.append(c)
        
        elif(c == ')'):
            try:
                stack.pop()
            
            except:
                return False

    if(len(stack) == 0):
        return True
    
    else:
        return False

print(balanced(input()))
