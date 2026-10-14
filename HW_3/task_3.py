n = int(input())
a = list(map(int, input().split()))
s = int(input())

path = []


def ssp(index, current_sum, taken):
    if index == n:
        return taken and current_sum == s

    path.append(a[index])

    if ssp(index + 1, current_sum + a[index], True):
        return True

    path.pop()

    if ssp(index + 1, current_sum, taken):
        return True

    return False


if ssp(0, 0, False):
    print("Yes")
    print(len(path))
    print(*path)
else:
    print("No")
