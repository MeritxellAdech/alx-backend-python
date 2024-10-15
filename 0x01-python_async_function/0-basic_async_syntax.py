#!/usr/bin/env python3
""" This module create a function that wait for a random amount of time"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """Generate a random value and returns it
    Args
        max_delay:float
        The mazimum amount of time wait_random whould delay
    Return
        The actual amount of time delayed
    """
    time = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
