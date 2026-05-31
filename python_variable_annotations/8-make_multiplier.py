#!/usr/bin/env python3
"""
This module writes a function make_multiplier
that takes a float multiplier as argument
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
