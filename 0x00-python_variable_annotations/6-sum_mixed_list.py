#!/usr/bin/env python3
""" This module implements a list of mixed types """
from typing import (List, Union)


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Adds the given list of numbers made up of ints and floats
    args
        mxd_lst:list[int, float] - the given list of numbers
    Return
        the sum total of given numbers
    """
    total: float = 0.0
    for n in mxd_lst:
        total += n
    return total
