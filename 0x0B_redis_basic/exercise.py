#!/usr/bin/env python3
""" Redis practice module """
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def replay(method: Callable):
    """ Replay function: displays the history of
    calls of a particular function. """
    r = redis.Redis()
    q_name = method.__qualname__

    inputs = r.lrange("{}:inputs".format(q_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(q_name), 0, -1)

    print("{} was called {} times:".format(q_name, int(r.get(q_name))))
    for input, output in zip(inputs, outputs):
        print("%s(*%s) -> %s" % (q_name, str(input)[2:-1], str(output)[2:-1]))


def call_history(method: Callable) -> Callable:
    """ Stores the called functions parameters in the Redis cache """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Temp """
        self._redis.rpush("{}:inputs".format(method.__qualname__),
                          str(args))
        output = method(self, *args)
        self._redis.rpush("{}:outputs".format(method.__qualname__),
                          str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Counts the amount of times Cache is called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            Uses method.__qualname__ as key to store the amount of times
        the decorated method is called. Conserves original functions name and
        docstring using functool.wraps()
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ Redis Cache class """

    def __init__(self):
        """
            Stores a private instance of Redis() in addition
            to resetting the current database upon initiliazation
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str, data: bytes) -> str:
        """  automatically parametrize Cache.get
        with the correct conversion function. """
        return self.get(key, str)

    def get_int(self, key: str, data: bytes) -> int:
        """  automatically parametrize Cache.get with
        the correct conversion function. """
        return self.get(key, int)
