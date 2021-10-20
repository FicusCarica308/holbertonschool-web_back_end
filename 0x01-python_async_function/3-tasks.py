#!/usr/bin/env python3
"""[summary]
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """[summary]
    A function that takes an integer called max_delay and returns a asyncio.Task
    Args:
        max_delay (int): The max sleep length of the wait_random function

    Returns:
        asyncio.Task: returns a asyncio task object to be await outside of
        this functions scope
    """
    return asyncio.create_task(wait_random(max_delay))
