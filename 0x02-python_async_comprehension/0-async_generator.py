#!/usr/bin/env python3
"""[summary]
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """[summary]

    Yields:
        Generator[int, None, None]: [description]
    """
    for i in range(11):
        yield uniform(0, 10)
        await asyncio.sleep(1)
