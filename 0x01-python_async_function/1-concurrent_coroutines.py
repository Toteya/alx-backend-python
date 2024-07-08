#!/usr/bin/env python3
"""
module:  1-concurrent_coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns the wait_random coroutine n number of times with the given max_delay
    and returns the a list of the delay values
    """
    delays: List[float] = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
