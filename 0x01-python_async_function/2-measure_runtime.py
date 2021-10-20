#!/usr/bin/env python3
"""[summary]
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the total execution time for
    wait_n(n, max_delay)
    Args:
        n (int): How many times the async function will be called
        max_delay (int): The max sleep time for each function call

    Returns:
        float: the total execution time of the entire program (total_time / n).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return ((end - start) / n)
