#!/usr/bin/env python3
""" 0x00. Python - Variable Annotations """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum a list of floats and ints"""
    return sum(mxd_lst)
    # return sum(map(lambda x: float(x), mxd_lst))
