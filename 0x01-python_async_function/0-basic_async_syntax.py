#!/usr/bin/env python3

'''
  0. The basics of async

  Author: Yusuf Mustapha Opeyemi
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    An asynchronous coroutine named wait_random that waits for
    a random delay between 0 and max_delay seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time that was waited.
    '''
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
