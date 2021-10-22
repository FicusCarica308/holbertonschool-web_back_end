#!/usr/bin/env python3
"""[summary]
"""
BaseCaching = __import__('0-basic_cache').BaseCaching

class FIFOCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    
    # overwrite of put function from BaseCaching
    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if (key is None or item is None):
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data):
            oldest_key = list(self.cache_data.keys())[0]
            print("DISCARD: {0}".format(oldest_key))
            self.cache_data.pop(oldest_key)
        self.cache_data[key] = item

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]