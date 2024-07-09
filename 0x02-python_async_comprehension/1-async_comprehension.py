#!/usr/bin/env python3
"""
module: 1-async_comprehension
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns a list of random numbers using an async comprehension
    """
    random_list = [x async for x in async_generator()]
    return random_list
