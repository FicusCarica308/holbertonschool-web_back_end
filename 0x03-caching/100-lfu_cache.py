#!/usr/bin/env python3
"""[summary]
"""
BaseCaching = __import__('0-basic_cache').BaseCaching


class LFUCache(BaseCaching):
    """[summary]

    Args:
        BaseCaching ([type]): [description]
    """
    __cache_data_usage = {}

    def __init__(self):
        """[summary]
        """
        super().__init__()

    def get_LFU(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        LFU_val = 0
        LFU_key = None
        for key in self.__cache_data_usage:
            if LFU_val == self.__cache_data_usage[key]:
                return None
            if LFU_val >= self.__cache_data_usage[key]:
                LFU_val = self.__cache_data_usage[key]
                LFU_key = key
        return LFU_key

    def put(self, key, item):
        """[summary]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if (key is None or item is None):
            return

        if (key in self.cache_data):
            self.get(key)  # moves existing node to front/ changes cache usage
            self.cache_data[key] = item
            return

        add = {key: item}
        add.update(self.cache_data)
        self.cache_data = add
        if (key not in self.__cache_data_usage):
            self.__cache_data_usage[key] = 1
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            LFU = self.get_LFU()
            if (LFU is not None):
                self.cache_data.pop(LFU)
                self.__cache_data_usage.pop(LFU)
                print("DISCARD: {0}".format(LFU))
            else:
                print("DISCARD: {0}".format(list(self.cache_data.keys())[-1]))
                self.__cache_data_usage.pop(list(self.cache_data.keys())[-1])
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
        self.__cache_data_usage[key] += 1
        return self.cache_data[key]

    def getter(self):
        """
        [summary]
        """
        print(self.__cache_data_usage)
