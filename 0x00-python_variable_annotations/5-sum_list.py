#!/usr/bin/env python3
""" This module implements List from typing """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Adds all numbers in the list
    args
        input_list: List[float] - a list array of float numbers
    Return
        The sum of all numbers in input_list
    """
    total: float = 0
    for n in input_list:
        total += n
    return total
