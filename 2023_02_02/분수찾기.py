ip = int(input())

sum = 0
ordL = 0
ordR = 0

for i in range(1, ip + 1):
    sum += i
    if sum >= ip:
        ordL = i
        ordR = ip - (sum - i)
        break

a = 0
b = 0

if ordL % 2 != 0:
    a = ordL + 1
    b = 0

    for j in range(ordR):
        a -= 1
        b += 1

elif ordL % 2 == 0:
    a = 0
    b = ordL + 1

    for j in range(ordR):
        b -= 1
        a += 1


print(str(a) + "/" + str(b))
