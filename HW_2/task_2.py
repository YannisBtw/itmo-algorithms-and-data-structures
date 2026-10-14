import sys

q = int(sys.stdin.readline())

capacity = 2 * q + 5
arr = [0] * capacity

left = q + 2
right = q + 2

answer = []

for _ in range(q):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        x = int(command[2])

        if command[1] == "back":
            arr[right] = x
            right += 1
        else:
            left -= 1
            arr[left] = x

    elif command[0] == "pop":
        if left == right:
            answer.append("Error")
        else:
            if command[1] == "front":
                answer.append(str(arr[left]))
                left += 1
            else:
                right -= 1
                answer.append(str(arr[right]))

    elif command[0] == "get":
        if left == right:
            answer.append("Error")
        else:
            if command[1] == "front":
                answer.append(str(arr[left]))
            else:
                answer.append(str(arr[right - 1]))

    elif command[0] == "size":
        answer.append(str(right - left))

print("\n".join(answer))
