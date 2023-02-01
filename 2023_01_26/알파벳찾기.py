ip = str(input())
op = ""
alp = {}
for i in range(97, 123):
    alp[str(chr(i))] = -1


for i in ip:
    alp[i] = ip.find(i)

for i in list(alp.values()):
    op += str(i)
    op += " "

print(op)
