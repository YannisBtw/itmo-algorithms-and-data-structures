numbers = map(int, input().split())

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

even.sort(reverse=True)
odd.sort(reverse=True)

answer = -1

if len(even) > 1:
    answer = max(answer, even[0] + even[1])

if len(odd) > 1:
    answer = max(answer, odd[0] + odd[1])

print(answer)
