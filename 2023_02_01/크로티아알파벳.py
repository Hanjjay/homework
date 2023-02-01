data = input()
ldata = len(data)
coraty = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

for i in coraty:
    if -1 != data.find(i):
        data = data.replace(i, "7")
        count += 1

print(len(data))
