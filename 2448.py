import math

triangle = ["  *   ", " * *  ", "***** "]


def starts(move):
    t = len(triangle)
    for i in range(t):
        triangle.append(triangle[i] + triangle[i])
        triangle[i] = ("   " * move + triangle[i] + "   " * move)


n = int(input())
q = int(math.log(int(n / 3), 2))

for i in range(q):
    starts(int(pow(2, i)))

for i in range(n):
    print(triangle[i])
# print(triangle)
