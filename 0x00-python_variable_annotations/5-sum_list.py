#!/usr/bin/env python3

'''
  Complex types - list of floats

  Author: Yusuf Mustapha Opeyemi
'''

from typing import Callable, Iterator, Union, Optional, List

def sum_list(input_list: List[float]) -> float:
    '''
      Returns the sum  of a list as a float.
    '''
    return sum(input_list)
