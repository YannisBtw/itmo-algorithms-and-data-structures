import sys

prices = list(map(int, sys.stdin.buffer.read().split()))
n = len(prices)

spans = [0] * n

for i in range(n):
    span = 1
    j = i - 1

    while j >= 0 and prices[j] <= prices[i]:
        span += spans[j]
        j -= spans[j]

    spans[i] = span

sys.stdout.write(" ".join(map(str, spans)))
