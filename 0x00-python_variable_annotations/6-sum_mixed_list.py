#!/usr/bin/env python3
""" 0x00. Python - Variable Annotations """


def sum_mixed_list(mxd_lst: list[mixed]) -> float:
    """ Sum a list of floats and ints """
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
    # return sum(map(lambda x: float(x), mxd_lst))
