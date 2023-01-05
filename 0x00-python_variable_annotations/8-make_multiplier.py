#!/usr/bin/env python3
""" 0x00. Python - Variable Annotations """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return a function"""
    def fn(n: float):
        return n * multiplier
    return fn
