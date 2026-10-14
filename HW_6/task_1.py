import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(root, x):
    if root is None:
        return Node(x)

    if x < root.key:
        root.left = add(root.left, x)
    elif x > root.key:
        root.right = add(root.right, x)

    return root


def exists(root, x):
    while root is not None:
        if x == root.key:
            return True
        elif x < root.key:
            root = root.left
        else:
            root = root.right

    return False


def find_min(root):
    while root.left is not None:
        root = root.left

    return root.key


def delete(root, x):
    if root is None:
        return None

    if x < root.key:
        root.left = delete(root.left, x)

    elif x > root.key:
        root.right = delete(root.right, x)

    else:
        if root.left is None and root.right is None:
            return None

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        min_key = find_min(root.right)
        root.key = min_key
        root.right = delete(root.right, min_key)

    return root


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def preorder(root, result):
    if root is None:
        return

    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)


q = int(sys.stdin.readline())

root = None
answer = []

for _ in range(q):
    command = sys.stdin.readline().split()

    if command[0] == "add":
        x = int(command[1])
        root = add(root, x)

    elif command[0] == "del":
        x = int(command[1])
        root = delete(root, x)

    elif command[0] == "exists":
        x = int(command[1])

        if exists(root, x):
            answer.append("YES")
        else:
            answer.append("NO")

    elif command[0] == "height":
        answer.append(str(height(root)))

    elif command[0] == "print":
        result = []
        preorder(root, result)

        if result:
            answer.append(" ".join(result))
        else:
            answer.append("Empty")

print("\n".join(answer))
