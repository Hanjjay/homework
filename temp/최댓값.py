ip = []
max = 0
while True:
    try:
        a = int(input())
        ip.append(a)
    except:
        break

for i in ip:
    if i > max:
        max = i

print(max)
print(ip.index(max) + 1)
