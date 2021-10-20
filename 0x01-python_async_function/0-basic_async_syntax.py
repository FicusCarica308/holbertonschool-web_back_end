#!/usr/bin/env python3
"""[summary]
    Module containing a python asynchronous coroutine
    Imports:
    asyncio - for await/async functionalitys
    random - random number generations
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    [summary]
     An asynchronous coroutine named wait_random. Waits for a random
     delay between 0 and 10 max_delay in seconds and
     eventually returns it.

    Args:
        max_delay (int, optional): A user given integer used to determine the
        length of the sleep. Defaults to 10.

    Returns:
        [float]: returns the amount in seconds the program slept for
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
