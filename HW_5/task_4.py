import heapq
import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
files = data[1:]

heapq.heapify(files)

total_cost = 0

while len(files) > 1:
    first = heapq.heappop(files)
    second = heapq.heappop(files)

    merged = first + second
    total_cost += merged

    heapq.heappush(files, merged)

print(total_cost)
