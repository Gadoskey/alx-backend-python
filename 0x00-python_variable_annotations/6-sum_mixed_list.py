#!/usr/bin/env python3

'''
  Complex types - mixed list

  Author: Yusuf Mustapha Opeyemi
'''

from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
      Takes a list of integers and floats and returns their sum as a float.
    '''
    return float(sum(mxd_lst))
