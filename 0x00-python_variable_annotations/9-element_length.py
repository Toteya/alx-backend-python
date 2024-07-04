#!/usr/bin/env python3
"""
module 9-element_length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the a list of tuples containing each element and its length
    """
    return [(i, len(i)) for i in lst]
