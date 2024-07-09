#!/usr/bin/env python3
"""
module: 2-measure_runtime
"""
import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    measures the runtime of four concurrent coroutines
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
