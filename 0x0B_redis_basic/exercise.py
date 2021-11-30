#!/usr/bin/env python3
""" Redis practice module """
import redis
from uuid import uuid4
from typing import Union


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
