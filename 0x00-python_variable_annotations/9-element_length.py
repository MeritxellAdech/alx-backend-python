#!/usr/bin/env python3
""" This module implements the calculation of length of a given list """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """the calculation of length of a given list

    args
        lst:iterable - a list
    Returns
        The length of given list
    """
    return [(i, len(i)) for i in lst]
