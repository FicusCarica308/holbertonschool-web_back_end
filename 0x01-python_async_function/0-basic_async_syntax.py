#!/usr/bin/env python3
"""[summary]
    temporary summary
"""
import asyncio
import typing
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
