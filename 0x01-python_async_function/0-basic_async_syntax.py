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
      a random delay between 0 and max_delay seconds and eventually returns it
    '''
    randomDelay = random.uniform(0, max_delay)
    await asyncio.sleep(randomDelay)
    return randomDelay
