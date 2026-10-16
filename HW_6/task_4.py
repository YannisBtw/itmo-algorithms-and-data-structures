import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = max(
            self._get_height(node.left),
            self._get_height(node.right)
        ) + 1

    def _get_balance(self, node):
        return (
            self._get_height(node.right)
            - self._get_height(node.left)
        )

    def _rotate_left(self, node):
        new_root = node.right

        node.right = new_root.left
        new_root.left = node

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _rotate_right(self, node):
        new_root = node.left

        node.left = new_root.right
        new_root.right = node

        self._update_height(node)
        self._update_height(new_root)

        return new_root

    def _balance(self, node):
        self._update_height(node)

        current_balance = self._get_balance(node)

        if current_balance == 2:
            if self._get_balance(node.right) < 0:
                node.right = self._rotate_right(node.right)

            return self._rotate_left(node)

        if current_balance == -2:
            if self._get_balance(node.left) > 0:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        return node

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)

        elif key > node.key:
            node.right = self._insert(node.right, key)

        else:
            return node

        return self._balance(node)

    def add(self, key):
        self.root = self._insert(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = node.right

            while successor.left is not None:
                successor = successor.left

            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return self._balance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

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

    def next_key(self, key):
        current = self.root
        candidate = None

        while current is not None:
            if current.key >= key:
                candidate = current.key
                current = current.left
            else:
                current = current.right

        return candidate

    def prev_key(self, key):
        current = self.root
        candidate = None

        while current is not None:
            if current.key <= key:
                candidate = current.key
                current = current.right
            else:
                current = current.left

        return candidate

    def root_key(self):
        if self.root is None:
            return None
        return self.root.key

    def height(self):
        return self._get_height(self.root)

    def preorder(self):
        result = []

        if self.root is None:
            return result

        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.key)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return result


def main():
    q = int(sys.stdin.readline())

    tree = AVLTree()
    answers = []

    for _ in range(q):
        command = sys.stdin.readline().split()
        operation = command[0]

        if operation == "add":
            key = int(command[1])
            tree.add(key)

        elif operation == "del":
            key = int(command[1])
            tree.delete(key)

        elif operation == "exists":
            key = int(command[1])
            answers.append("YES" if tree.exists(key) else "NO")

        elif operation == "next":
            key = int(command[1])
            answers.append(str(tree.next_key(key)))

        elif operation == "prev":
            key = int(command[1])
            answers.append(str(tree.prev_key(key)))

        elif operation == "root":
            root_key = tree.root_key()
            answers.append(
                str(root_key) if root_key is not None else "Empty"
            )

        elif operation == "height":
            answers.append(str(tree.height()))

        elif operation == "print":
            traversal = tree.preorder()

            if traversal:
                answers.append(" ".join(map(str, traversal)))
            else:
                answers.append("Empty")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()