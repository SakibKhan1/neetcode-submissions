class MyHashSet:

    
    def __init__(self):
        self.size = 769
        self.buckets = [[] for _ in range(self.size)]
        
    def hashfunction(self, value):
        return value % 769

    def add(self, key: int) -> None:
        index = self.hashfunction(key)
        bucket = self.buckets[index]
        if key not in bucket: 
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self.hashfunction(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self.hashfunction(key)
        bucket = self.buckets[index]
        if key in bucket:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)