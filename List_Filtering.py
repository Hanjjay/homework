def filter_list(ip):
    op = []
    for i in range(len(ip)):
        if (type(ip[i]) == int):
            op.append(ip[i])
    return op