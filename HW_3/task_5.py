n = int(input())

moves = []


def hanoi(k, start, finish, extra):
    if k == 0:
        return

    hanoi(k - 1, start, extra, finish)

    moves.append((k, start, finish))

    hanoi(k - 1, extra, finish, start)


hanoi(n, 1, 3, 2)

print(len(moves))

for move in moves:
    print(*move)
