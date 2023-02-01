data = list(map(str, input().split()))


ip = []

ip.append(int(data[0][::-1]))
ip.append(int(data[1][::-1]))

if ip[0] > ip[1]:
    print(ip[0])
else:
    print(ip[1])
