#!/usr/bin/env python3

'''
   Duck typing - first element of a sequence
  Author: Yusuf Mustapha Opeyemi
'''
from typing import Any, Union, Sequence, Iterable, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ code augmentation """
    if lst:
        return lst[0]
    else:
        return None
