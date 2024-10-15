#!/usr/bin/env python3

'''
  4. Tasks

  Author: Yusuf Mustapha Opeyemi
'''

import asyncio
from typing import List

# importing task_wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Function to alter wait_n into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being called.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for each call.

    Returns:
        List[float]: A list of floats.
    '''
    # Create tasks list
    tasks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
