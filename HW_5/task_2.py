import heapq
import sys

data = list(map(int, sys.stdin.buffer.read().split()))

k = data[0]
index = 1

arrays = []
heap = []

for array_id in range(k):
    length = data[index]
    index += 1

    current_array = data[index:index + length]
    index += length

    arrays.append(current_array)

    heapq.heappush(heap, (current_array[0], array_id, 0))

answer = []

while heap:
    value, array_id, position = heapq.heappop(heap)

    answer.append(value)

    next_position = position + 1

    if next_position < len(arrays[array_id]):
        next_value = arrays[array_id][next_position]
        heapq.heappush(heap, (next_value, array_id, next_position))

sys.stdout.write(" ".join(map(str, answer)))

# Второй способ

data = list(map(int, sys.stdin.buffer.read().split()))

k = data[0]

numbers = []

index = 1

for _ in range(k):
    length = data[index]
    index += 1

    for _ in range(length):
        numbers.append(data[index])
        index += 1

numbers.sort()

print(*numbers)
