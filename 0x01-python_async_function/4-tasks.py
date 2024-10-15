#!/usr/bin/env python3

'''
  4. Tasks

  Author: Yusuf Mustapha Opeyemi
'''

import asyncio
from typing import List

# importing wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function to measure the total execution time for wait_n(n, max_delay),
    and return the average time per call.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for each call.

    Returns:
        float: The average time per execution.
    '''
    # Create task
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
