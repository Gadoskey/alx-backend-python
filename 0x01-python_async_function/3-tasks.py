#!/usr/bin/env python3

'''
  3. Tasks

  Author: Yusuf Mustapha Opeyemi
'''

from asyncio import Task, create_task

# importing wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    '''
    Function task_wait_random that takes an integer max_delay.
    Returns a asyncio.Task.

    Args:
        max_delay (int): Maximum delay for each call.

    Returns:
        Task: A asyncio task.
    '''
    # Create task
    task = create_task(wait_random(max_delay))
    return task
