#!/usr/bin/env python3
"""
    Practice Async Comprehension
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[summary]
    A coroutine that will collect 10 random numbers using an async
    comprehensing over async_generator (from 0-async_generator),
    then return the 10 random numbers.
    Returns:
        List[float]: List of float results yielded by async_generator()
    """
    return ([yielded_item async for yielded_item in async_generator()])
