import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
k = data[1]

a = data[2:]

a.sort()

print(a[k - 1])
