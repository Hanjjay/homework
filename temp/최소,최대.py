empty = input()
ip = list(map(int, input().split()))
op = ""
ip.sort()

op = op + str(ip[0]) + " " + str(ip[-1])
print(op)
