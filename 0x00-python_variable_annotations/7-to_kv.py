#!/usr/bin/env python3
"""
[summary]
Contains a single python function definition this time using
complex type annotations (inputs Union (int | float) typing and Tuple typing)
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """[summary]

    Args:
        k (str): a string that will be returned unmodified
        v (Union[int, float]): A number that can be either int or float
        which will be squared

    Returns:
        Tuple[str, float]: Returns a tuple with the first value being a str
        and the second being a float (typed using typing Tuple class)
    """
    return (k, float(pow(v, 2)))
