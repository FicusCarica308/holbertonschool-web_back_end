#!/usr/bin/env python3
"""[summary]
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]
    Imports task_wait_random then uses an async
    routine called task_wait_n that takes in 2 int arguments (in this order): n
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
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
