import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(root, key, nodes):
    new_node = Node(key)
    nodes[key] = new_node

    if root is None:
        return new_node

    current = root
    parent = None

    while current is not None:
        parent = current

        if key < current.key:
            current = current.left
        else:
            current = current.right

    new_node.parent = parent

    if key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

    return root


def rotate_left(root, node):
    right_child = node.right
    beta = right_child.left
    parent = node.parent

    right_child.parent = parent

    if parent is None:
        root = right_child
    elif parent.left is node:
        parent.left = right_child
    else:
        parent.right = right_child

    right_child.left = node
    node.parent = right_child

    node.right = beta

    if beta is not None:
        beta.parent = node

    return root


def rotate_right(root, node):
    left_child = node.left
    beta = left_child.right
    parent = node.parent

    left_child.parent = parent

    if parent is None:
        root = left_child
    elif parent.left is node:
        parent.left = left_child
    else:
        parent.right = left_child

    left_child.right = node
    node.parent = left_child

    node.left = beta

    if beta is not None:
        beta.parent = node

    return root


def preorder(root, result):
    if root is None:
        return

    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)


n = int(sys.stdin.readline())
keys = list(map(int, sys.stdin.readline().split()))

root = None
nodes = {}

for key in keys:
    root = insert(root, key, nodes)

m = int(sys.stdin.readline())

answer = []

for _ in range(m):
    command, value = sys.stdin.readline().split()
    value = int(value)

    node = nodes[value]

    if command == "left":
        root = rotate_left(root, node)
    else:
        root = rotate_right(root, node)

    result = []
    preorder(root, result)
    answer.append(" ".join(result))

print("\n".join(answer))
