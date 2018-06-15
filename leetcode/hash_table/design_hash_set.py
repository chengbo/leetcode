class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [None] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        bucket = self.__find_bucket(key)
        if bucket is None:
            self.buckets[self.__get_bucket_index(key)] = [key]
            return
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        bucket = self.__find_bucket(key)
        if bucket is None:
            return
        if key not in bucket:
            return
        bucket.remove(key)

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        bucket = self.__find_bucket(key)
        if bucket is None:
            return False
        return key in bucket

    def __get_bucket_index(self, key):
        return key % self.size

    def __find_bucket(self, key):
        bucket_index = self.__get_bucket_index(key)
        return self.buckets[bucket_index]
