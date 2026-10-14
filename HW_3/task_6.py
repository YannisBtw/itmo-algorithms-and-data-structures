n = int(input())

used_cols = set()
used_diag1 = set()
used_diag2 = set()

path = []
answers = []


def queens(row):
    if row == n + 1:
        answers.append(path.copy())
        return

    for col in range(1, n + 1):
        diag1 = row - col
        diag2 = row + col

        if col in used_cols:
            continue

        if diag1 in used_diag1:
            continue

        if diag2 in used_diag2:
            continue

        path.append(col)
        used_cols.add(col)
        used_diag1.add(diag1)
        used_diag2.add(diag2)

        queens(row + 1)

        path.pop()
        used_cols.remove(col)
        used_diag1.remove(diag1)
        used_diag2.remove(diag2)


queens(1)

print(len(answers))

for answer in answers:
    print(*answer)
