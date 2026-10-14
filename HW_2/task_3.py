tokens = input().split()

stack = []

for token in tokens:
    if token == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)

    elif token == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)

    elif token == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)

    else:
        stack.append(int(token))

print(stack[0])
