#!/usr/bin/env python3
"""
Defines a coroutine that gathers random values from an async generator
using asynchronous comprehension.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Executes the async generator and builds a list of 10 floats
    produced during its iteration.
    """
    results = [num async for num in async_generator()]
    return results
