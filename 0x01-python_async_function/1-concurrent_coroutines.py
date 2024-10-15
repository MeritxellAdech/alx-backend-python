#!/usr/bin/env python3
""" This module creates an async function wait_n """
import asyncio
from typing import List
from random import uniform

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random an n times with a random delay
    Args
        n:int
        The number of times wait_random is executed
        max_delay: int
            The waiting time
    Return
        A sorted list of all floating numbers genereated
    """
    unordered: List = []
    for _ in range(n):
        unordered.append(await wait_random(max_delay))

    return sorted(unordered)
