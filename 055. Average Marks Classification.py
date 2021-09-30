# Conditional 1

def main(a, b, c):
    averageMarks = (a + b + c) / 3
    if a < 0 or b < 0 or c < 0 or a > 100 or b > 100 or c > 100:
        print('INVALID MARKS')
    else:
        if averageMarks >= 70:
            print('DISTINCTION')
        elif averageMarks >= 60 and averageMarks < 70:
            print('FIRST')
        elif averageMarks >= 50 and averageMarks < 60:
            print('SECOND')
        elif averageMarks >= 40 and averageMarks < 50:
            print('THIRD')
        elif averageMarks >= 0 and averageMarks < 40:
            print('FAIL')

            
a = int(input())
b = int(input())
c = int(input())
main(a,b,c)
