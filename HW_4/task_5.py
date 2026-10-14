import sys

n = int(sys.stdin.buffer.readline())

participants = []

for _ in range(n):
    login, solved, penalty = sys.stdin.buffer.readline().split()

    solved = int(solved)
    penalty = int(penalty)

    participants.append((-solved, penalty, login))

participants.sort()

answer = []

for solved, penalty, login in participants:
    answer.append(login)

sys.stdout.buffer.write(b"\n".join(answer))
