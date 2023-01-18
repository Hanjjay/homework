ip = []

while True:
    try:
        a = int(input())
        ip.append(a % 42)
    except:
        break

ip = list(set(ip))

print(len(ip))
