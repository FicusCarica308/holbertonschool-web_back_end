#! /usr/bin/env python3
from typing import List as list
"""[summary]
"""


def sum_list(input_list: list[float]) -> float:
    """[summary]

    Args:
        input_list (list[float]): [description]

    Returns:
        float: [description]
    """
    sum = 0
    for num in input_list:
        sum += num
    return(sum)
