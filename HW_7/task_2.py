import sys


class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.color = "R"
        self.left = None
        self.right = None
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, node):
        new_root = node.right

        node.right = new_root.left

        if new_root.left is not None:
            new_root.left.parent = node

        new_root.parent = node.parent

        if node.parent is None:
            self.root = new_root
        elif node is node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

        new_root.left = node
        node.parent = new_root

    def _rotate_right(self, node):
        new_root = node.left

        node.left = new_root.right

        if new_root.right is not None:
            new_root.right.parent = node

        new_root.parent = node.parent

        if node.parent is None:
            self.root = new_root
        elif node is node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

        new_root.right = node
        node.parent = new_root

    def insert(self, key):
        parent = None
        current = self.root

        while current is not None:
            parent = current

            if key == current.key:
                return

            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node = Node(key, parent)

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.parent is not None and node.parent.color == "R":
            parent = node.parent
            grandparent = parent.parent

            if parent is grandparent.left:
                uncle = grandparent.right

                if uncle is not None and uncle.color == "R":
                    parent.color = "B"
                    uncle.color = "B"
                    grandparent.color = "R"

                    node = grandparent

                else:
                    if node is parent.right:
                        node = parent
                        self._rotate_left(node)

                        parent = node.parent
                        grandparent = parent.parent

                    parent.color = "B"
                    grandparent.color = "R"
                    self._rotate_right(grandparent)

            else:
                uncle = grandparent.left

                if uncle is not None and uncle.color == "R":
                    parent.color = "B"
                    uncle.color = "B"
                    grandparent.color = "R"

                    node = grandparent

                else:
                    if node is parent.left:
                        node = parent
                        self._rotate_right(node)

                        parent = node.parent
                        grandparent = parent.parent

                    parent.color = "B"
                    grandparent.color = "R"
                    self._rotate_left(grandparent)

        self.root.color = "B"

    def exists(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return True

            if key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def root_key(self):
        if self.root is None:
            return None

        return self.root.key

    def preorder(self):
        if self.root is None:
            return "Empty"

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()

            result.append(f"{node.key}{node.color}")

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return " ".join(result)


def main():
    q = int(sys.stdin.buffer.readline())

    tree = RedBlackTree()
    answers = []

    for _ in range(q):
        command = sys.stdin.buffer.readline().split()
        operation = command[0]

        if operation == b"add":
            key = int(command[1])
            tree.insert(key)

        elif operation == b"exists":
            key = int(command[1])
            answers.append("YES" if tree.exists(key) else "NO")

        elif operation == b"root":
            key = tree.root_key()
            answers.append(str(key) if key is not None else "Empty")

        elif operation == b"print":
            answers.append(tree.preorder())

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
