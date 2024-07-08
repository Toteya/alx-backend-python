#!/usr/bin/env python3
"""
module 2-measure_runtime
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for the wait_n function
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    exec_time = time.time() - start_time
    return exec_time
