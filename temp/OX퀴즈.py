cnt = int(input())

for i in range(cnt):
    op = 0
    fever = 1
    ip = str(input())

    for i in ip:
        if i == "O":
            op += fever
            fever += 1
        else:
            fever = 1
    print(op)
