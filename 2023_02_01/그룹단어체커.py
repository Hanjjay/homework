case = int(input())

for i in range(case):

    ip = list(input())

    for j in range(len(ip) - 1):

        if ip[j] == ip[j + 1]:
            pass
        elif ip[j] in ip[j + 2 :]:
            case -= 1
            break

print(case)
