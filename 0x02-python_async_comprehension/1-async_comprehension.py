#!/usr/bin/env python3

'''
  1. Async Comprehensions

  Author: Yusuf Mustapha Opeyemi
'''

from asyncio import sleep
from random import uniform
from typing import Generator, List

# importing async_generator
async_generator = __import__('0-async_generator').async_generator

def async_comprehension() -> List[float]:
    '''
    Function async_comprehension that takes no arguments.
    It collect 10 random numbers using an async comprehensing over async_generator,
    then return the 10 random numbers.

    Args:
        none

    Returns:
        float:A nNumber between 0 and 10.
    '''
    # Gets and returns the 10 random numbers.
    random_number = [i async for i in async_generator()]
    return random_number
