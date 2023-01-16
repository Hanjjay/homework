ip = list(map(int, input().split()))  # 세줄 리스트로 입력받기


def dice(ip):
    top_ip = 0
    # 가장큰 값
    for i in ip:
        if top_ip < i:
            top_ip = i

    for i in range(len(ip)):
        cnt = ip.count(ip[i])
        if cnt == 3:
            return print(10000 + (ip[1] * 1000))
        elif cnt == 2:
            return print(1000 + (ip[i] * 100))

    return print(top_ip * 100)


dice(ip)
