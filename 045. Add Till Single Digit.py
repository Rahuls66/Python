def main(n):
    sum = 0
    while int(n) > 9:
        l = (map(int, str(n)))
        for i in l:
            sum += i
    print(int(sum))

main(345)
