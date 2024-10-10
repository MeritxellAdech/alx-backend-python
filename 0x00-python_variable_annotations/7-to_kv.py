#!/usr/bin/env python3
""" This module implements complex types
    where a variable could be of one or another type
"""
from typing import (Union, Tuple)


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert given parameters to tuple and square the second
    Args
        k:str - Any given string
        v:int|float - any given number
    Return
        The tuple in the following way (k, v^2)
    """
    return (k, v**2)
