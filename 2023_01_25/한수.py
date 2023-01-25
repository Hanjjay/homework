ip = int(input())


def hansu(ip):
    if ip > 100:
        return ip
    else:
        op = []
        st = []
        for i in range(100, ip + 1):
            sp_i = list(map(int, str(i)))
            idx1 = 0
            idx2 = 1
            for s in range(len(sp_i) - 1):
                st.append(sp_i[idx1] - sp_i[idx2])
                idx1 += 1
                idx2 += 1
            st = set(st)
            if len(st) == 1:
                op.append(i)
            st = []
        return len(op) + 99


print(hansu(ip))
