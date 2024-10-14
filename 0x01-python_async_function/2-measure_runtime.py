#!/usr/bin/env python3

'''
  2. Measure the runtime

  Author: Yusuf Mustapha Opeyemi
'''

import time
import asyncio

# importing wait_n
wait_n = __import__('1_concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''
    Function to measure the total execution time for wait_n(n, max_delay),
    and return the average time per call.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: The average time per execution.
    '''
    # Record the start time
    start_time = time.time()

    # Run the wait_n function
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end_time = time.time()

    # Calculate the total time elapsed
    total_time = end_time - start_time

    # Return the average time per call
    return total_time / n
