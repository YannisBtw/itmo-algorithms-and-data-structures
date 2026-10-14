import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
a = data[1:1 + n]
s = data[1 + n]

seen = {}

for i in range(n):
    x = a[i]
    need = s - x

    if need in seen:
        print(seen[need], i + 1)
        sys.exit()

    if x not in seen:
        seen[x] = i + 1

print(-1)
