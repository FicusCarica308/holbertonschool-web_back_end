#!/usr/bin/env python3
"""[summary]
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class LIFOCache(BaseCaching):
    """[summary]
    Args:
        BaseCaching ([type]): [description]
    """
    ____last_key_in = None

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
            self.cache_data[key] = item
            self.__last_key_in = key
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            print("DISCARD: {0}".format(self.__last_key_in))
            self.cache_data.pop(self.__last_key_in)

        self.cache_data[key] = item
        self.__last_key_in = key
