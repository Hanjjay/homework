# 여러줄 데이터 입력 참고 https://inhyeokyoo.github.io/algorithm/stdin/

import sys

num = int(sys.stdin.readline())
op = []

for i in range(30):
    op.append(i + 1)

while True:
    try:
        empty = map(int, sys.stdin.readline())
        op.remove(empty)
    except:
        break

op.sort()
print(op[0])
print(op[1])
