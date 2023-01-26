import sys

temp = input()
while True:
    try:

        op = ""
        cnt, ip = map(str, sys.stdin.readline().split())
        for i in ip:
            for j in range(int(cnt)):
                op += i
        print(op)

    except:
        break
