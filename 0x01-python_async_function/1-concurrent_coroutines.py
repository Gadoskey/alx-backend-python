#!/usr/bin/env python3

'''
  1. Let's execute multiple coroutines at the same time with async

  Author: Yusuf Mustapha Opeyemi
'''

import asyncio
from random import uniform
from typing import List

# importing wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Asynchronous coroutine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    '''
    # Create a list of coroutines
    coroutines = [wait_random(max_delay) for i in range(n)]
    
    # Gather results of all coroutines
    results = await asyncio.gather(*coroutines)

    # Manually sort the results using a simple algorithm (like insertion sort)
    sorted_results = []
    for result in results:
        # Insert in sorted order
        inserted = False
        for i in range(len(sorted_results)):
            if result < sorted_results[i]:
                sorted_results.insert(i, result)
                inserted = True
                break
        if not inserted:
            sorted_results.append(result)

    return sorted_results
