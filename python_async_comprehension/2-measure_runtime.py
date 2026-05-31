#!/usr/bin/env python3
"""
Contains a coroutine for timing parallel execution of multiple
async comprehension calls.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs the async_comprehension coroutine 4 times concurrently,
    tracks how long it takes, and returns the duration.
    """
    start = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    finish = time.time()
    return finish - start
