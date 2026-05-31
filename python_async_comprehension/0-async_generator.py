#!/usr/bin/env python3
"""
Module defining an async generator that produces random numbers
with a delay between each value.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields 10 random floating-point values.
    Each value is produced after a non-blocking delay of 1 second.
    """
    for i in range(10):
        await asyncio.sleep(1)
        value = random.uniform(0, 10)
        yield value
