import sys

q = int(sys.stdin.readline())

queue = []
head = 0
size = 0

answer = []

for _ in range(q):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(int(command[1]))
        size += 1

    elif command[0] == "pop":
        if size == 0:
            answer.append("Error")
        else:
            answer.append(str(queue[head]))
            head += 1
            size -= 1

    elif command[0] == "get":
        if size == 0:
            answer.append("Error")
        else:
            answer.append(str(queue[head]))

    elif command[0] == "size":
        answer.append(str(size))

print("\n".join(answer))
