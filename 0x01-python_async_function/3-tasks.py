#!/usr/bin/env python3

'''
  3. Tasks

  Author: Yusuf Mustapha Opeyemi
'''

from asyncio import Task, create_task

# importing wait_n
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
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
    task = create_task(wait_random(max_delay))
    return task
