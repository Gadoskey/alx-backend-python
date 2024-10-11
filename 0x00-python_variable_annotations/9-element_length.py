#!/usr/bin/env python3

'''
  Let's duck type an iterable object
  Author: Yusuf Mustapha Opeyemi
'''
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Annotated function. Return values with the appropriate types '''
    return [(i, len(i)) for i in lst]
