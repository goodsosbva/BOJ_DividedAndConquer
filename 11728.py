import sys

n, m = map(int, sys.stdin.readline().split())

l1 = list(map(int, sys.stdin.readline().split()))
l2 = list(map(int, sys.stdin.readline().split()))

l3 = l1 + l2
ans = " ".join(map(str, sorted(l3)))
print(ans)



