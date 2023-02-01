def wordcheck():

    ip = str(input())
    ip = ip.upper()
    op = "?"
    max = 0
    maxindex = 0

    for i in range(len(ip)):
        if max < ip.count(ip[i]):
            max = ip.count(ip[i])
            maxindex = i

    for i in range(len(ip)):
        if max == ip.count(ip[i]) and ip[maxindex] != ip[i]:
            return print(op)
    op = ip[maxindex]
    return print(op)
