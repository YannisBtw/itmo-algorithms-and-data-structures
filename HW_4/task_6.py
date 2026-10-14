import sys

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
m = data[1]

segments = []

index = 2

for _ in range(m):
    left = data[index]
    right = data[index + 1]
    segments.append((left, right))
    index += 2

segments.sort()

covered = 0

current_left, current_right = segments[0]

for left, right in segments[1:]:
    if left <= current_right + 1:
        if right > current_right:
            current_right = right
    else:
        covered += current_right - current_left + 1
        current_left = left
        current_right = right

covered += current_right - current_left + 1

print(n - covered)
