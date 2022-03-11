#!/usr/bin/env python3
""" function that make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function make_multiplier that
    takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier
    """
    def f(x):
        return x * multiplier
    return f
