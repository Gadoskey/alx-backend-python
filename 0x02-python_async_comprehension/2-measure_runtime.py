#!/usr/bin/env python3

'''
  2. Run time for four parallel comprehensions

  Author: Yusuf Mustapha Opeyemi
'''

from asyncio import gather
from time import time

# importing async_comprehension
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Function measure_runtime that takes no arguments.
    The coroutine will execute async_comprehension
    four times in parallel using asyncio.gather.

    Args:
        none

    Returns:
        float:The total runtime of the function
    '''
    # Record the start time
    start_time = time()

    # Run the async_comprehension function
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)

    # Record the end time
    end_time = time()

    # Calculate the total time elapsed
    total_time = end_time - start_time

    # Return the average time per call
    return total_time
