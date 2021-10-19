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
    
     an asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10)
     named wait_random that waits for a random delay between 0 and max_delay (included and float value)
     seconds and eventually returns it.

    Args:
        max_delay (int, optional): A user given integer used to determine the
        length of the sleep. Defaults to 10.

    Returns:
        [float]: returns the amount in seconds the program slept for
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
