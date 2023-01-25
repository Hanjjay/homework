case = int(input())
for i in range(case):
    ip = list(map(int, input().split()))
    count = 0
    sum = 0

    for i in range(1, len(ip)):
        sum += ip[i]

    average = sum / (len(ip) - 1)

    for i in range(1, len(ip)):
        if ip[i] > average:
            count += 1
    op = (count / (len(ip) - 1)) * 100
    print("%0.3f" % op + "%")
