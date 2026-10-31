import sys


def main():
    n, k = map(int, sys.stdin.buffer.readline().split())
    users = list(map(int, sys.stdin.buffer.readline().split()))

    freq = {}

    for i in range(k):
        user = users[i]
        freq[user] = freq.get(user, 0) + 1

    answer = [str(len(freq))]

    for i in range(k, n):
        leaving = users[i - k]

        freq[leaving] -= 1

        if freq[leaving] == 0:
            del freq[leaving]

        entering = users[i]
        freq[entering] = freq.get(entering, 0) + 1

        answer.append(str(len(freq)))

    print(" ".join(answer))


if __name__ == "__main__":
    main()
