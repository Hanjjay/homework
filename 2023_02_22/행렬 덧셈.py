N, M = map(int, input().split())
lst = []
lst2 = []
op = []

for i in range(N):
    lst.append(list(map(int, input().split())))

for i in range(N):
    lst2.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        op.append(lst[i][j] + lst2[i][j])

for i in range(N):
    print(*op[:M])
    del op[:M]
