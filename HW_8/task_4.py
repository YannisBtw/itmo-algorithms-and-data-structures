# https://contest.yandex.ru/contest/102171/run-report/170004051/

import sys


class Entry:
    __slots__ = ("key", "value", "hash_value", "next")

    def __init__(self, key, value, hash_value, next_entry=None):
        self.key = key
        self.value = value
        self.hash_value = hash_value
        self.next = next_entry


class HashTable:
    def __init__(self):
        self._buckets = [None] * 8
        self._size = 0

    def _hash(self, key):
        h = 14695981039346656037

        for char in key:
            h ^= char
            h = (h * 1099511628211) & 0xFFFFFFFFFFFFFFFF

        return h

    def _resize(self):
        new_capacity = len(self._buckets) * 2
        new_buckets = [None] * new_capacity
        mask = new_capacity - 1

        for head in self._buckets:
            current = head

            while current is not None:
                next_entry = current.next

                index = current.hash_value & mask

                current.next = new_buckets[index]
                new_buckets[index] = current

                current = next_entry

        self._buckets = new_buckets

    def put(self, key, value):
        hash_value = self._hash(key)
        index = hash_value & (len(self._buckets) - 1)

        current = self._buckets[index]

        while current is not None:
            if current.hash_value == hash_value and current.key == key:
                current.value = value
                return

            current = current.next

        new_entry = Entry(
            key, value, hash_value, self._buckets[index]
        )

        self._buckets[index] = new_entry
        self._size += 1

        if self._size * 4 > len(self._buckets) * 3:
            self._resize()

    def get(self, key):
        hash_value = self._hash(key)
        index = hash_value & (len(self._buckets) - 1)

        current = self._buckets[index]

        while current is not None:
            if current.hash_value == hash_value and current.key == key:
                return current.value

            current = current.next

        return None

    def delete(self, key):
        hash_value = self._hash(key)
        index = hash_value & (len(self._buckets) - 1)

        current = self._buckets[index]
        previous = None

        while current is not None:
            if current.hash_value == hash_value and current.key == key:
                if previous is None:
                    self._buckets[index] = current.next
                else:
                    previous.next = current.next

                self._size -= 1
                return current.value

            previous = current
            current = current.next

        return None

    def size(self):
        return self._size


def main():
    q = int(sys.stdin.buffer.readline())

    table = HashTable()
    answers = []

    for _ in range(q):
        command = sys.stdin.buffer.readline().split()
        operation = command[0]

        if operation == b"put":
            key = command[1]
            value = int(command[2])

            table.put(key, value)

        elif operation == b"get":
            key = command[1]
            value = table.get(key)

            answers.append("Error" if value is None else str(value))

        elif operation == b"del":
            key = command[1]
            value = table.delete(key)

            answers.append("Error" if value is None else str(value))

        elif operation == b"size":
            answers.append(str(table.size()))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
