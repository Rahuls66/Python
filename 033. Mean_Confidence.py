#Calculate the mean Confidence of X-DSPAM and Y-DSPAM given in the list Data

def conf():
    Data = [' X-DSPAM-Confidence:0.8475 ',' X-DSPAM-Confidence:0.765 ',
            ' X-DSPAM-Confidence:0.7065 ','Y-DSPAM-Confidence:0.9985 ',
            'Y-DSPAM-Confidence:0.6585 ']
    x_values = 0
    x_count = 0
    y_values = 0
    y_count = 0

    for string in Data:
        spam = string.strip()
        if spam.startswith("X-DSPAM"):
            x_values += float(spam.split(':')[1])
            x_count += 1
    
        if spam.startswith("Y-DSPAM"):
            y_values += float(spam.split(':')[1])
            y_count += 1
    print(f"Mean X-Confidence : {x_values / x_count}")
    print(f"Mean Y-Confidence : {y_values / y_count}")
    
conf()

'''
Expected Output:
Mean X-Confidence : 0.773
Mean Y-Confidence : 0.8285
'''
