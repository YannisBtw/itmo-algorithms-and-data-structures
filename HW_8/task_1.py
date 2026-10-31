import sys


def main():
    n = int(sys.stdin.buffer.readline())

    groups = {}
    max_group = 0

    for _ in range(n):
        word = sys.stdin.buffer.readline().strip()
        key = bytes(sorted(word))

        groups[key] = groups.get(key, 0) + 1

        max_group = max(max_group, groups[key])

    print(len(groups), max_group)


if __name__ == "__main__":
    main()
