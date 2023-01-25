def selfnumber(n):
    ip = n
    while n != 0:
        ip = ip + n % 10
        n = n // 10
    return ip


op = []
for i in range(1, 10000):
    num = selfnumber(i)
    op.append(num)
    if not i in op:
        print(i)
