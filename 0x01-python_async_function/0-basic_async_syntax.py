#!/usr/bin/env python3
""""
module 0-basic_async_syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine that wait for a random delay between 0 and the given
    max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    print(delay)

    return delay
