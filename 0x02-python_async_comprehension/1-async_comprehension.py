#!/usr/bin/env python3
"""[summary]
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[summary]

    Returns:
        List[float]: [description]
    """
    return ([yielded_item async for yielded_item in async_generator()])
