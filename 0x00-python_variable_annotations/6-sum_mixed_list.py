#!/usr/bin/env python3
"""
[summary]
Contains a single python function definition this time using
complex type annotations (inputs Union from typing for subscriptable
List class and int | float typing)
"""
from typing import Union

def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """[summary]

    Args:
        mxd_lst (Union[int, float]): a list of either integer or floats

    Returns:
        float: sum of all number in mxd_lst
    """
    sum = 0
    for num in mxd_lst:
        sum += num
    return(sum)
