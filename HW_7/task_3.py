import sys
from bisect import bisect_left


class BTree:
    def __init__(self, keys, children):
        self.keys = keys
        self.children = children

    def search(self, target):
        current = 1
        visited = []

        while True:
            visited.append(str(current))

            node_keys = self.keys[current]
            position = bisect_left(node_keys, target)

            if position < len(node_keys) and node_keys[position] == target:
                return "YES " + " ".join(visited)

            node_children = self.children[current]

            if not node_children:
                return "NO " + " ".join(visited)

            current = node_children[position]


def main():
    input = sys.stdin.buffer.readline

    n = int(input())

    keys = [[] for _ in range(n + 1)]
    children = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        data = list(map(int, input().split()))

        k = data[0]

        keys[i] = data[1:k + 1]
        children[i] = data[k + 2:]

    tree = BTree(keys, children)

    q = int(input())
    answers = []

    for _ in range(q):
        target = int(input())
        answers.append(tree.search(target))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
