n = int(input())
if 4 <= n <= 1000:
    a = [[0] * n for i in range(n)]
    cnt = 1
    b = 0
    c = 0
    i = 0
    while cnt <= n ** 2:
        for j in range(b, n - c):
            a[i][j] = cnt
            cnt += 1
        b += 1
        for i in range(b, n - c):
            a[i][j] = cnt
            cnt += 1
        for j in range(n - 1 - b, -1 + c, -1):
            a[i][j] = cnt
            cnt += 1
        c += 1
        for i in range(n - 1 - b, -1 + c, -1):
            a[i][j] = cnt
            cnt += 1
    for i in a:
        for j in i:
            print(j, ' ', end='')
        print()
else:
    print('Введите число от 4 до 1000')