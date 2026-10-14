import heapq
import sys

q = int(sys.stdin.buffer.readline())

low = []
high = []

answer = []

for _ in range(q):
    request = sys.stdin.buffer.readline().split()

    if request[0] == b"ADD":
        x = int(request[1])

        if not low or x <= -low[0]:
            heapq.heappush(low, -x)
        else:
            heapq.heappush(high, x)

        if len(low) < len(high):
            value = heapq.heappop(high)
            heapq.heappush(low, -value)

        if len(low) > len(high) + 1:
            value = -heapq.heappop(low)
            heapq.heappush(high, value)

    else:
        answer.append(str(-low[0]))

sys.stdout.write("\n".join(answer))
