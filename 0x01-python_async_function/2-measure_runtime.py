#!/usr/bin/env python3
""" This module contains the measure_time function """

from time import perf_counter
from asyncio import run


def measure_time(n: int, max_delay: int) -> float:
    """Calculates the total execution time for wait_n to get executed
    Args
        n:int
            The number of times wait_n should be executed
        max_delay:int
            The time delayed
    Return
        the total execution time taken"""
    start: float = perf_counter()
    run(__import__("1-concurrent_coroutines").wait_n(n, max_delay))
    end: float = perf_counter()

    return (end - start) / n
