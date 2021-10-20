#!/usr/bin/env python3
"""[summary]
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]
    Imports wait_random from the previous python file then uses an async
    routine called wait_n that takes in 2 int arguments (in this order): n
    and max_delay. You will spawn wait_random n times with the specified
    max_delay.

    Args:
        n (int): How many times the async function will be called
        max_delay (int): The max sleep time for each function call

    Returns:
        List[float]: returns a list of sleep delay times as floats from each
        async call(await)
    """
    tasks = list()
    delays = list()
    for i in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
