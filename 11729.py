pole = int(input())
cnt = 0


def hanoi(pole, Circle, SubCircle, ToCircle):
    if pole == 1:
        res.append([Circle, ToCircle])

    else:
        hanoi(pole - 1, Circle, ToCircle, SubCircle)
        hanoi(1, Circle, SubCircle, ToCircle)
        hanoi(pole - 1, SubCircle, Circle, ToCircle)


res = []
hanoi(pole, 1, 2, 3)
# print(res)
print(len(res))
print("\n".join(([" ".join(str(i) for i in row) for row in res])))
