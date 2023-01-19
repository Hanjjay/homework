import sys

cnt = input()  # emppty로 미리 한줄을 받을시 아래 while문에서는 읽지않는다

ip = list(map(int, sys.stdin.readline().split()))
max = 0

for i in ip:
    if max < i:
        max = i
