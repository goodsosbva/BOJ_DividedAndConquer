n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

# print(paper)

res1 = 0
resMinus1 = 0
res0 = 0


def cuting(x, y, n):
    global res1, resMinus1, res0
    config = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if config != paper[i][j]:
                for q in range(3):
                    for w in range(3):
                        cuting(x + n // 3 * q, y + n // 3 * w, n // 3)
                return
    if config == 1:
        res1 += 1
    elif config == -1:
        resMinus1 += 1
    else:
        res0 += 1

cuting(0, 0, n)
print(resMinus1)
print(res0)
print(res1)
