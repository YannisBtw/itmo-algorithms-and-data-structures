n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

answer = []

top = 0
bottom = n - 1
left = 0
right = m - 1

while top <= bottom and left <= right:
    for col in range(left, right + 1):
        answer.append(matrix[top][col])
    top += 1

    for row in range(top, bottom + 1):
        answer.append(matrix[row][right])
    right -= 1

    if top <= bottom:
        for colr2l in range(right, left - 1, -1):
            answer.append(matrix[bottom][colr2l])
        bottom -= 1

    if left <= right:
        for rowb2t in range(bottom, top - 1, -1):
            answer.append(matrix[rowb2t][left])
        left += 1

print(*answer)
