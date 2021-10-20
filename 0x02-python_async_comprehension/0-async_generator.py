#!/usr/bin/env python3
"""
    Practice asynchronous generator
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """[summary]
    A coroutine that will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10.
    Yields:
        Generator[float, None, None]: A random generated float number
        typed using the typing librarys built in Generator Type
    """
    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
