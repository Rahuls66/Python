def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    
    if (num > 999) or (num < 1):
        print('INVALID_INPUT')
    else:
        print(bin(num).replace("0b", ""))
 
