import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
a = data[1:]

values = sorted(set(a))
rank = {value: i + 1 for i, value in enumerate(values)}

compressed = [rank[x] for x in a]

size = len(values)
fenwick = [0] * (size + 1)

inversions = 0

for r in reversed(compressed):
    index = r - 1
    current_sum = 0

    while index > 0:
        current_sum += fenwick[index]
        index -= index & -index

    inversions += current_sum

    index = r

    while index <= size:
        fenwick[index] += 1
        index += index & -index

print(inversions)
