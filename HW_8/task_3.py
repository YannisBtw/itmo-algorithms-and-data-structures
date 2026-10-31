import sys


def main():
    n, s = map(int, sys.stdin.buffer.readline().split())
    numbers = map(int, sys.stdin.buffer.read().split())

    count = {0: 1}

    prefix_sum = 0
    answer = 0

    for number in numbers:
        prefix_sum += number

        needed = prefix_sum - s

        answer += count.get(needed, 0)

        count[prefix_sum] = count.get(prefix_sum, 0) + 1

    print(answer)


if __name__ == "__main__":
    main()
