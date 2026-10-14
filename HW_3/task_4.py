from math import comb

n, k = map(int, input().split())

path = []
answer = []


def dfs(start):
    if len(path) == k:
        answer.append(path.copy())
        return

    for number in range(start, n + 1):
        path.append(number)
        dfs(number + 1)
        path.pop()


dfs(1)

print(comb(n, k))

for combination in answer:
    print(*combination)
