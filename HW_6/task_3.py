import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    if node is None:
        return 0

    return node.height


def update_height(node):
    node.height = max(
        get_height(node.left),
        get_height(node.right)
    ) + 1


def get_balance(node):
    return get_height(node.right) - get_height(node.left)


def rotate_left(node):
    new_root = node.right

    node.right = new_root.left
    new_root.left = node

    update_height(node)
    update_height(new_root)

    return new_root


def rotate_right(node):
    new_root = node.left

    node.left = new_root.right
    new_root.right = node

    update_height(node)
    update_height(new_root)

    return new_root


def balance(node):
    update_height(node)

    current_balance = get_balance(node)

    if current_balance == 2:
        if get_balance(node.right) < 0:
            node.right = rotate_right(node.right)

        return rotate_left(node)

    if current_balance == -2:
        if get_balance(node.left) > 0:
            node.left = rotate_left(node.left)

        return rotate_right(node)

    return node


def add(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = add(node.left, key)

    elif key > node.key:
        node.right = add(node.right, key)

    else:
        return node

    return balance(node)


def exists(root, key):
    current = root

    while current is not None:
        if key == current.key:
            return True

        elif key < current.key:
            current = current.left

        else:
            current = current.right

    return False


def preorder(root):
    if root is None:
        return "Empty"

    result = []
    stack = [root]

    while stack:
        node = stack.pop()

        result.append(str(node.key))

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

    return " ".join(result)


q = int(sys.stdin.readline())

root = None
answer = []

for _ in range(q):
    command = sys.stdin.readline().split()

    if command[0] == "add":
        key = int(command[1])
        root = add(root, key)

    elif command[0] == "exists":
        key = int(command[1])

        if exists(root, key):
            answer.append("YES")
        else:
            answer.append("NO")

    elif command[0] == "root":
        if root is None:
            answer.append("Empty")
        else:
            answer.append(str(root.key))

    elif command[0] == "height":
        answer.append(str(get_height(root)))

    elif command[0] == "print":
        answer.append(preorder(root))

sys.stdout.write("\n".join(answer))
