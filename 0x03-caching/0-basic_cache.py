#!/usr/bin/env python3
"""
[summary]
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """[summary]
    """
    
    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if (key is None or item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        """[summary]

        Args:
            key ([type]): [description]
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
