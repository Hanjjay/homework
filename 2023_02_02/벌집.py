ip = int(input())
layer = int(((ip / 3) ** (1 / 2)))

while True:
    if ip <= 3 * layer * layer - 3 * layer + 1:
        break
    layer += 1

if ip == 1:
    print(ip)
else:
    print(layer)
