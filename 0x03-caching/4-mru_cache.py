#!/usr/bin/env python3
"""[summary]
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class MRUCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    __most_recent_access = None

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
        if (key is None or item is None):
            return

        if (key in self.cache_data):
            self.__most_recent_access = key
            self.cache_data[key] = item
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            self.cache_data.pop(self.__most_recent_access)
            print("DISCARD: {0}".format(self.__most_recent_access))
        self.cache_data[key] = item
        self.__most_recent_access = key

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]
        """
        if (key is None or key not in self.cache_data):
            return None
        self.__most_recent_access = key
        return self.cache_data[key]
