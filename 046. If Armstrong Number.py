def main():
    num = input()
    sum = 0
    if len(num) == 3:
        for i in num:
            sum = int(i)**3 + sum
        if sum == int(num):
            print('ARMSTRONG')
        else:
            print('NOT ARMSTRONG')
    else:
        print('INVALID_INPUT')

main()
