import sys

sys.setrecursionlimit(200000)

n, m = map(int, input().split())

memo = [-1] * (n + 1)


def fib(k):
    if k == 0 or k == 1:
        return 1 % m

    if memo[k] != -1:
        return memo[k]

    memo[k] = (fib(k - 1) + fib(k - 2)) % m
    return memo[k]


print(fib(n))
