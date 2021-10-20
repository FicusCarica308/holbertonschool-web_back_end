#!/usr/bin/env python3
"""[summary]
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """[summary]

    Yields:
        Generator[float, None, None]: [description]
    """
    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
