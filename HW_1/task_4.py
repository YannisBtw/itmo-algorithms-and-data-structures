numbers = map(int, input().split())

total = 0
min_odd = 10 ** 9

for number in numbers:
    total += number

    if number % 2 == 1:
        min_odd = min(min_odd, number)

if total % 2 == 0:
    answer = total
else:
    answer = total - min_odd

print(answer)
