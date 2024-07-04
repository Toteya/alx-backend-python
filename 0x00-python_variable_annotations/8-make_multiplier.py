#!/usr/bin/env python3
"""
module: 8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a multiplier function that multiplies a float by the given
    multiplier
    """
    def multiply(num: float) -> float:
        return num * multiplier

    return multiply
