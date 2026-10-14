import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
m = data[1]

a = data[2:2 + n]
b = data[2 + n:2 + n + m]

i = 0
j = 0

answer = []

while i < n and j < m:
    if a[i] <= b[j]:
        answer.append(str(a[i]))
        i += 1
    else:
        answer.append(str(b[j]))
        j += 1

while i < n:
    answer.append(str(a[i]))
    i += 1

while j < m:
    answer.append(str(b[j]))
    j += 1

sys.stdout.write(" ".join(answer))
