ip = list(map(int, input().split()))
ip2 = list(map(int, input().split()))
op = []
for i in range(len(ip2)):
    if ip2[i] < ip[1]:
        op.append(ip[i])
print(op)
