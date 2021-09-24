def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if (pow(a, 2) == (pow(b, 2) + pow(c,2))) and (a>b and b>c and a>c):
        print('RIGHT ANGLE TRIANGLE')
        
    elif pow(a,2) != (pow(b, 2) + pow(c,2)) and (a>b and b>c and a>c):
        print('NOT RIGHT ANGLE TRIANGLE')
        
    else:
        print('INVALID_INPUT')
        
main()
