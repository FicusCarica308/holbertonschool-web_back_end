#!/usr/bin/env python3
"""[summary]
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [description]
    """
    if (n == 0):
        return [await wait_random(max_delay)]
    tasks = list()
    for i in range(n):
        tasks.append(wait_random(max_delay))
    L = await asyncio.gather(*tasks)
    return L
