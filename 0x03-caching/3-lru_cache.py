#!/usr/bin/env python3
"""[summary]
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class LRUCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    def __init__(self):
        """[summary]
        """
        super().__init__()

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if (key in self.cache_data):
            self.get(key) # moves existing node to front
            self.cache_data[key] = item
            return
            
        add = {key: item}
        add.update(self.cache_data)
        self.cache_data = add
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            print("DISCARD: {0}".format(list(self.cache_data.keys())[-1]))
            self.cache_data.popitem()

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]
        """
        if (key is None or key not in self.cache_data):
            return None
        # move located node to front of dictionary
        hold_data = self.cache_data[key]
        self.cache_data.pop(key)
        self.put(key, hold_data)
        return self.cache_data[key]
