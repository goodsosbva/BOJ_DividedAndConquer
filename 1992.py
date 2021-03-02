n = int(input())
res = ""
quadTree = []
for i in range(n):
    quadTree.append(list(map(int, ''.join(input()))))

# paper = [list(map(str, input().split())) for _ in range(n)]


def cuting(x, y, n):
    global quadTree, res
    config = quadTree[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if config != quadTree[i][j]:
                res += "("

                for q in range(2):
                    for w in range(2):
                        cuting(x + n // 2 * q, y + n // 2 * w, n // 2)

                """
                cuting(x, y, n // 2)  
                cuting(x, y + n // 2, n // 2)
                cuting(x + n // 2, y, n // 2)
                cuting(x + n // 2, y + n // 2, n // 2)
                """
                res += ")"
                return
    if config == 1:
        res += "1"
    else:
        res += "0"

# print(paper)
# print(quadTree)
cuting(0, 0, n)
print(res)
