numbers = list(map(int, input().split()))

total = sum(numbers)

rem1 = []
rem2 = []

for number in numbers:
    if number % 3 == 1:
        rem1.append(number)
    elif number % 3 == 2:
        rem2.append(number)

rem1.sort()
rem2.sort()

if total % 3 == 0:
    answer = total

elif total % 3 == 1:
    candidates = []

    if len(rem1) >= 1:
        candidates.append(rem1[0])

    if len(rem2) >= 2:
        candidates.append(rem2[0] + rem2[1])

    answer = total - min(candidates)

else:
    candidates = []

    if len(rem2) >= 1:
        candidates.append(rem2[0])

    if len(rem1) >= 2:
        candidates.append(rem1[0] + rem1[1])

    answer = total - min(candidates)

print(answer)
