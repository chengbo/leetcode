class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [None] * self.size

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket = self.__find_bucket(key)
        if bucket is None:
            self.buckets[self.__get_bucket_index(key)] = [[key, value]]
            return
        pair = next((pair for pair in bucket if pair[0] == key), None)
        if pair is None:
            bucket.append([key, value])
        else:
            pair[1] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket = self.__find_bucket(key)
        if bucket is None:
            return -1
        pair = next((pair for pair in bucket if pair[0] == key), None)
        if pair is None:
            return -1
        return pair[1]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket = self.__find_bucket(key)
        if bucket is None:
            return
        pair = next((pair for pair in bucket if pair[0] == key), None)
        if pair is None:
            return
        bucket.remove(pair)

    def __get_bucket_index(self, key):
        return key % self.size

    def __find_bucket(self, key):
        bucket_index = self.__get_bucket_index(key)
        return self.buckets[bucket_index]
