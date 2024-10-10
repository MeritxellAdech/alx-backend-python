#!/usr/bin/env python3
""" This module implements function returning function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies its parameter by multiplier
    Args
        multiplier:float - the given number
    Return
        A function that takes a floating number
    """

    def inner_make_multiplier(n: float) -> float:
        """Multiplies n by multiplier
        Args
            n:float - Any given number
        Return
            The product of n times multiplier
        """
        return n * multiplier

    return inner_make_multiplier
