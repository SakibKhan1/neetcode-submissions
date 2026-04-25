class MyHashMap:

    def __init__(self):
        self.size = 769
        self.buckets = [[] for _ in range(self.size)]

    def hashfunction(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hashfunction(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update
                return

        bucket.append((key, value))  # insert

    def get(self, key: int) -> int:
        index = self.hashfunction(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        index = self.hashfunction(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)