#!/usr/bin/python3
""" fifo-Cache """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifco-cache """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            self.order.append(key)
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.order[0]]
                    print("DISCARD:", self.order[0])
                    self.order.pop(0)
                self.cache_data[key] = item

    def get(self, key):
        """
        return value
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
