#!/usr/bin/env python3
"""
module: 0-async_generator
"""
import asyncio
import random


async def async_generator():
    """
    Asynchronously generates 10 random floats between 0 and 10
    """
    count = 0
    while count < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        count += 1
