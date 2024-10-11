#!/usr/bin/env python3

'''
  Complex types - functions
  Author: Yusuf Mustapha Opeyemi
'''
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
       Function make_multiplier that takes a float multiplier as argument.
       Returns a function that multiplies a float by multiplier.
    '''
    def mul(number: float) -> float:
        ''' Mulitiplies a float by multipler '''
        return float(number * multiplier)
    
    return mul
