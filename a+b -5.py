import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a + b == 0:
            break
        print(a + b)
    except:
        break

# 여러줄 두칸 입력받기
