#!/usr/bin/env python3
"""
module 7-to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the given string and the square of the given
    number
    """
    return (k, v ** 2)
