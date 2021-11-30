#!/usr/bin/env python3
""" Redis practice module """
import redis
from uuid import uuid4
from typing import Union, Callable


class Cache():
    """ Redis Cache class """

    def __init__(self):
        """
            Stores a private instance of Redis() in addition
            to resetting the current database upon initiliazation
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores given data to our current redis session database """
        random_key = uuid4()
        random_key = str(random_key)
        self._redis.mset({random_key: data})
        return random_key

    def get(self, key: str, fn: Callable = None):
        """
        Returns a value from a given key in the Redis cache...
        Optional argument 'fn' can be used to convert the returned
        value into a requested type.

        EXP (int): Cache.get(key, int) -> returns integer
        Cache.store("example_key", 123)
        Cache.get("example_key", int) -> returns 123 instead of b"123"
        """
        value = self._redis.get(key)
        if fn is not None and value is not None:
            return fn(value)
        return value
