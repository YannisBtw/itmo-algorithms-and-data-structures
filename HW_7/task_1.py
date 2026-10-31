import sys


def validate(node, lower, upper, parent_is_red):
    if node == 0:
        return 0

    key = keys[node]

    if lower is not None and key <= lower:
        return -1

    if upper is not None and key >= upper:
        return -1

    is_red = colors[node] == b"R"

    if parent_is_red and is_red:
        return -1

    left_height = validate(
        left_children[node],
        lower,
        key,
        is_red
    )

    if left_height == -1:
        return -1

    right_height = validate(
        right_children[node],
        key,
        upper,
        is_red
    )

    if right_height == -1:
        return -1

    if left_height != right_height:
        return -1

    if is_red:
        return left_height

    return left_height + 1


def main():
    global keys, colors, left_children, right_children

    n = int(sys.stdin.buffer.readline())

    keys = [0] * (n + 1)
    colors = [b""] * (n + 1)
    left_children = [0] * (n + 1)
    right_children = [0] * (n + 1)

    for i in range(1, n + 1):
        key, color, left, right = sys.stdin.buffer.readline().split()

        keys[i] = int(key)
        colors[i] = color
        left_children[i] = int(left)
        right_children[i] = int(right)

    if colors[1] != b"B":
        print("NO")
        return

    black_height = validate(1, None, None, False)

    if black_height == -1:
        print("NO")
    else:
        print("YES", black_height)


if __name__ == "__main__":
    main()
