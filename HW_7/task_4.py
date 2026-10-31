import sys
from bisect import bisect_left


class Node:
    __slots__ = ("keys", "children")

    def __init__(self) -> None:
        self.keys = []
        self.children = []

    def is_leaf(self) -> bool:
        return not self.children


class BTree:
    def __init__(self, t: int) -> None:
        self.t = t
        self.root = None
        self.inserted_keys = set()

    def is_full(self, node) -> bool:
        return len(node.keys) == 2 * self.t - 1

    def height(self) -> int:
        h = 0
        node = self.root

        while node is not None:
            h += 1
            node = None if node.is_leaf() else node.children[0]

        return h

    def levels(self) -> list:
        result = []
        level = [self.root] if self.root is not None else []

        while level:
            result.extend(level)
            level = [child for node in level for child in node.children]

        return result

    def find(self, key: int) -> bool:
        node = self.root

        while node is not None:
            i = bisect_left(node.keys, key)

            if i < len(node.keys) and node.keys[i] == key:
                return True

            if not node.children:
                return False

            node = node.children[i]

        return False

    def split_child(self, parent, i: int) -> None:
        child = parent.children[i]
        t = self.t

        middle_key = child.keys[t - 1]

        right_child = Node()
        right_child.keys = child.keys[t:]
        right_child.children = child.children[t:]

        child.keys = child.keys[:t - 1]
        child.children = child.children[:t]

        parent.keys.insert(i, middle_key)
        parent.children.insert(i + 1, right_child)

    def insert(self, key: int) -> None:
        if key in self.inserted_keys:
            return

        self.inserted_keys.add(key)

        if self.root is None:
            self.root = Node()
            self.root.keys.append(key)
            return

        max_keys = 2 * self.t - 1

        if len(self.root.keys) == max_keys:
            new_root = Node()
            new_root.children.append(self.root)

            self.split_child(new_root, 0)
            self.root = new_root

        node = self.root

        while node.children:
            i = bisect_left(node.keys, key)
            child = node.children[i]

            if len(child.keys) == max_keys:
                self.split_child(node, i)

                if key > node.keys[i]:
                    i += 1

                child = node.children[i]

            node = child

        i = bisect_left(node.keys, key)
        node.keys.insert(i, key)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t, q = int(data[0]), int(data[1])
    pos = 2

    tree = BTree(t)
    out = []

    for _ in range(q):
        cmd = data[pos]

        if cmd == b"add":
            tree.insert(int(data[pos + 1]))
            pos += 2

        elif cmd == b"exists":
            out.append("YES" if tree.find(int(data[pos + 1])) else "NO")
            pos += 2

        elif cmd == b"root":
            out.append(
                " ".join(map(str, tree.root.keys))
                if tree.root is not None else "Empty"
            )
            pos += 1

        elif cmd == b"height":
            out.append(str(tree.height()))
            pos += 1

        else:
            nodes = tree.levels()
            out.append(
                " ".join(
                    "[" + " ".join(map(str, node.keys)) + "]"
                    for node in nodes
                ) if nodes else "Empty"
            )
            pos += 1

    sys.stdout.write("".join(line + "\n" for line in out))


if __name__ == "__main__":
    main()
