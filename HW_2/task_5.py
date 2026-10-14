pushed = list(map(int, input().split()))
popped = list(map(int, input().split()))

stack = []
j = 0

for number in pushed:
    stack.append(number)

    while stack and stack[-1] == popped[j]:
        stack.pop()
        j += 1

if j == len(popped):
    print("True")
else:
    print("False")
