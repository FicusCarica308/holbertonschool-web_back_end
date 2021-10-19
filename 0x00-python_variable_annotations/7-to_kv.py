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
        k (str): [description]
        v (Union[int, float]): [description]

    Returns:
        Tuple[str, float]: [description]
    """
    return (k, floar(pow(v, 2)))
