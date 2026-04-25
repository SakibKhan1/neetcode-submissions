class MyHashSet:
    def __init__(self):
        self.size = 769          # prime number to reduce collisions
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.buckets[index]
