a, b = map(int, (input(), input()))  # 두줄 입력받기
if a > 0:
    if b > 0:
        print(1)
    else:
        print(4)
if a < 0:
    if b > 0:
        print(2)
    else:
        print(3)
