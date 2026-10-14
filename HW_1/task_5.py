numbers = list(map(int, input().split()))

rem0 = []
rem1 = []
rem2 = []

for number in numbers:
    if number % 3 == 0:
        rem0.append(number)
    elif number % 3 == 1:
        rem1.append(number)
    elif number % 3 == 2:
        rem2.append(number)

answer = -1

rem0.sort(reverse=True)
rem1.sort(reverse=True)
rem2.sort(reverse=True)

if len(rem0) >= 2:
    answer = max(answer, rem0[0] + rem0[1])

if len(rem1) >= 1 and len(rem2) >= 1:
    answer = max(answer, rem1[0] + rem2[0])

print(answer)
