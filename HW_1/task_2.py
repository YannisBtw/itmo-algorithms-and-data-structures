n, m = map(int, input().split())

digits = input().strip()

rem = 0
ans = []

for char in digits:
    digit = int(char)
    rem = (rem * 10 + digit) % m
    ans.append(rem)

print(*ans)
