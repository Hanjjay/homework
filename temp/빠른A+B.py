import sys

empty = input()  # emppty로 미리 한줄을 받을시 아래 while문에서는 읽지않는다

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break
