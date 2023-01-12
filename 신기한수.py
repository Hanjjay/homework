
ip = int(input())

cnt = 0

for i in range(1,ip+1):

    s_ip = sum( map (int, str(i))) #각 자리수 합

    if(i%s_ip == 0):
        cnt += 1
        
print(cnt)    