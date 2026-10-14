import sys

data = sys.stdin.buffer.read().split()

numbers = data[1:]

numbers.sort(key=lambda x: x * 10, reverse=True)

result = b"".join(numbers)

if result[0] == ord("0"):
    print(0)
else:
    sys.stdout.buffer.write(result)
