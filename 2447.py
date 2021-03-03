def starts(n):
    if n == 3:
        drawing[0][:3] = drawing[2][:3] = [1] * 3
        drawing[1][:3] = [1, 0, 1]
    else:
        t = n // 3
        starts(n // 3)
        for q in range(3):
            for w in range(3):
                if q == 1 and w == 1:
                    continue
                for v in range(t):
                    drawing[t * q + v][t * w: t * (w + 1)] = drawing[v][:t]


n = int(input())
drawing = [[0 for i in range(n)] for i in range(n)]

starts(n)

for i in drawing:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
