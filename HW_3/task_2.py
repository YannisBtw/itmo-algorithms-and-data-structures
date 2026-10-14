n = int(input())
a = list(map(int, input().split()))
s = int(input())


def ssp(index, current_sum, taken):
    if index == n:
        return taken and current_sum == s

    take = ssp(index + 1, current_sum + a[index], True)

    if take:
        return True

    not_take = ssp(index + 1, current_sum, taken)

    return not_take


if ssp(0, 0, False):
    print("Yes")
else:
    print("No")
