#!/usr/bin/env python3

'''
  0. Async Generator

  Author: Yusuf Mustapha Opeyemi
'''

from asyncio import sleep
from random import uniform
from typing import Generator


def async_generator() -> Generator[float, None, None]:
    '''
    Function async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.

    Args:
        none

    Returns:
        float:A nNumber between 0 and 10.
    '''
    # The coroutine will loop 10 times
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
